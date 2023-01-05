# Use firefox addons inside playwright 

## Tools needed
* Playwright (https://playwright.dev)
* Python (https://www.python.org)
* geckordp (https://jpramosi.github.io/geckordp/)

## How to do

Use **Playwright** to create a firefox browser instance. Make sure to specify "--start-debugger-server" to allow **geckordp** to connect.

```python
browser = playwright.firefox.launch(headless=False, args=["--start-debugger-server", str(debug_port)])
```


Use **geckordp** *RDPClient* to connect to launched browser instance

```python
client = RDPClient(60)
client.connect("localhost", debug_port)
```

Get *AddonsActor* from *RootActor* from connected *RDPClient*

```python
root = RootActor(client)
root_actor_ids = root.get_root()

addon_actor_id = root_actor_ids["addonsActor"]

addon_actor = AddonsActor(client, addon_actor_id)
```

Use *install_temporary_addon* to perform xpi addon installation

```python
response = addon_actor.install_temporary_addon(addon_path)
addon_id = response.get("id", None)
```

If *addon_id* is not *None* addon was installed succesfully

```python
installed = not (addon_id is None)
```

**Have fun!**
