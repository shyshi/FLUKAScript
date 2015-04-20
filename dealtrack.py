import matplotlib.pyplot as plt;
f1=open("./NEUTRON_tab.lis")
usrtracklines=["a"]
pointx=["a"];
pointy=["a"];
for s in f1.readlines():
    if s.startswith(" #"):
        continue
    else:
        usrtracklines.append(s);
        temp=s.split();
        pointx.append(float(temp[0]));
        y=float(temp[1])-float(temp[0]);
        y=y*float(temp[2]);
        pointy.append(y);
pointx.remove("a");
pointy.remove("a");
print(len(pointx));
print(len(pointy));
xmax=max(pointx)
ymax=max(pointy)
plt.loglog(lw=2)
plt.xlim(1e-13,0.1)
plt.ylim(1e-11,ymax)
plt.plot(pointx,pointy);
plt.show()
