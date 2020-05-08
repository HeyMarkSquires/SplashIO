color("green")
cube([60,130,5]);
difference(){
  translate([20,0, 5]){
      color("blue")
      cube([5,130,15]);
   }
   translate([18,55,5]){
       color("red")
       cube([20,20,4]);  
    } 
    }
    difference(){
        translate([30,0, 5]){
          color("blue")
          cube([5,130,15]);
        }
        translate([18,55,5]){
   color("red")
   cube([20,20,4]);  
}
    }
difference(){
    translate([25,0,5]){
      cube([5,130,5]);
    }
    translate([18,55,5]){
   color("red")
   cube([20,20,4]);  
}
}


    