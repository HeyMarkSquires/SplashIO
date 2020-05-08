
translate([-30,-20, 100]){
    color("orange")
    cube([245,50,5]);
}
difference(){
    translate([7.5,5, 85]){
        color("blue")
        cube([170,5,15]);
    }
    translate([82.5,-7,95]){
        cube([20,50,5]);
    }
}

difference(){
    translate([7.5,-6, 85]){
        color("blue")
        cube([170,5,15]);
    }
    translate([82.5,-7,95]){
        cube([20,50,5]);
    }
}

difference(){
    translate([7.5,-1, 95]){
        cube([170,6, 5]);
    }
    translate([82.5,-7,95]){
        cube([20,50,5]);
    }
}


