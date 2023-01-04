from playwright.sync_api import Playwright
from geckordp.rdp_client import RDPClient
from geckordp.actors.root import RootActor
from geckordp.actors.addon.addons import AddonsActor


def install_addon(addon_actor, addon_path) -> bool:
    response = addon_actor.install_temporary_addon(addon_path)
    addon_id = response.get("id", None)
    return not (addon_id is None)

def prepare_browser(playwright: Playwright, debug_port: int):
    browser = playwright.firefox.launch(headless=False, args=["--start-debugger-server", str(debug_port)])

    context = browser.new_context()
   
    client = RDPClient(60)
    client.connect("localhost", debug_port)

    root = RootActor(client)
    root_actor_ids = root.get_root()

    addon_actor_id = root_actor_ids["addonsActor"]

    addon_actor = AddonsActor(client, addon_actor_id)

    return (browser, context, addon_actor)






