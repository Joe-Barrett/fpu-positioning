getSelectionCoordinates(xpoints, ypoints)
x = xpoints[0]
y = ypoints[0]
call("ij.plugin.frame.ThresholdAdjuster.setMode", "B&W");
setThreshold(0, 60);
setOption("BlackBackground", false);
run("Convert to Mask");
run("Invert")
run("Despeckle")
run("Specify...", "width=120 height=120 x=x y=y oval centered");
run("Measure")
run("Open Next")
