from pathlib import Path
import json
root=Path(__file__).parent
resources={"css":(root/"site.css").read_text(encoding="utf-8"),"runtime":(root/"runtime.js").read_text(encoding="utf-8")}
(root/"resources.js").write_text("window.FORGE_RESOURCES = "+json.dumps(resources,ensure_ascii=True)+";\n",encoding="utf-8")
print("Preview and export resources refreshed.")
