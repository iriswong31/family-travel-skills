#!/usr/bin/env python3
"""Create a local registry or approve a prepared trip; no networking."""
import argparse,json,datetime
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument("action",choices=["init","approve","show"])
p.add_argument("registry",type=Path)
p.add_argument("--name",default="旅行足迹")
p.add_argument("--manifest",type=Path)
a=p.parse_args()
if a.action=="init":
 if a.registry.exists():raise SystemExit("Registry exists; refusing overwrite")
 a.registry.parent.mkdir(parents=True,exist_ok=True)
 data={"series":a.name,"latest_approved_trip":None,"trips":[]}
elif a.action=="show":
 print(a.registry.read_text());raise SystemExit(0)
else:
 if not a.manifest:raise SystemExit("--manifest required after user approval")
 data=json.loads(a.registry.read_text());trip=json.loads(a.manifest.read_text())
 ids=[r["id"] for r in data["trips"]]
 expected="TRIP %03d"%(max([int(i.split()[-1]) for i in ids]+[0])+1)
 if trip.get("id")!=expected:raise SystemExit("Expected "+expected)
 image=(a.manifest.parent/trip.get("image","")).resolve()
 if not image.is_file():raise SystemExit("Approved image missing")
 if trip.get("manufacturing_status")=="verified" and not trip.get("outline_svg"):
  raise SystemExit("Verified manufacture requires outline")
 for edge in trip.get("shared_edges",[]):
  if edge.get("reference_trip") not in ids:raise SystemExit("Unknown neighbor")
  if not edge.get("curve_file"):raise SystemExit("Shared curve required")
  if not (a.manifest.parent/edge["curve_file"]).is_file():raise SystemExit("Shared curve file missing")
 trip["status"]="user_approved_visual"
 trip["confirmed_at"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
 trip["image"]=str(image)
 data["trips"].append(trip);data["latest_approved_trip"]=trip["id"]
out=a.registry.with_suffix(".tmp")
out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
out.replace(a.registry)
print(a.registry)
