 public class Main
{
    /* 
     * black gray darkGray eyeOne eyeTwo brownOne brownTwo 
     * bkgdOne bkgdTwo white offWhite trunks green green2

    */
    public static void main(String[] args)
    {
        //background
        Square back = new Square();
        back.setY(0);
        back.setX(0);
        back.changeSize(1000);
        back.changeColor("bases");
        back.makeVisible();
        
        //background
        Square backgro = new Square();
        backgro.setY(-800);
        backgro.setX(200);
        backgro.changeSize(1000);
        backgro.rotate(40);
        backgro.setTransparency(50);
        backgro.changeColor("green2");
        backgro.makeVisible();
        
        
        //background
        Square backgr = new Square();
        backgr.setY(500);
        backgr.setX(-300);
        backgr.changeSize(1300);
        backgr.rotate(40);
        backgr.setTransparency(50);
        backgr.changeColor("green");
        backgr.makeVisible();

        //background
        Triangle backg = new Triangle();
        backg.changeSize(1000, 1800);
        backg.setX(1000);
        backg.setY(-120);
        backg.rotate(-20);
        backg.changeColor("bkgdTwo");
        backg.setTransparency(50);
        backg.makeVisible();

    //trunk
    Rect trunk = new Rect();
        trunk.changeColor("trunks");
        trunk.changeSize(100, 1400);
        trunk.setX(-500);
        trunk.setY(160);
        trunk.rotate(88);
        trunk.makeVisible();
        //end of backing
            
                  //body
                  Ellipse body = new Ellipse (230,175);
                    body.setX(210);
                    body.setY(300);
                    body.changeColor("offWhite");
                    body.rotate(90);
                    body.makeVisible();
            
                  //arms
                    Ellipse arm = new Ellipse (150,50);
                    arm.setX(160);
                    arm.setY(410);
                    arm.changeColor("offWhite");
                    arm.rotate(20);
                    arm.makeVisible();
                  
                    Ellipse arms = new Ellipse (150,50);
                    arms.setX(150);
                    arms.setY(300);
                    arms.changeColor("offWhite");
                    arms.rotate(40);
                    arms.makeVisible();
                  
            
                   //head
                    Ellipse cranial = new Ellipse (150,122);
                    cranial.setX(220);
                    cranial.setY(190);
                    cranial.changeColor("offWhite");
                    cranial.rotate(5);
                    cranial.makeVisible();
            
                  //face
                  Ellipse face = new Ellipse (100,80);
                    face.setX(235);
                    face.setY(205);
                    face.changeColor("gray");
                    face.rotate(5);
                    face.makeVisible();
            
                    //snout
            
                  Ellipse snout = new Ellipse (40,40);
                    snout.setX(263);
                    snout.setY(240);
                    snout.changeColor("darkGray");
                    snout.rotate(90);
                    snout.makeVisible();
            
                  //eyes begin
                    Circle eye1 = new Circle();
                    eye1.changeColor("eyeOne");
                    eye1.setX(250);
                    eye1.setY(230);
                    eye1.changeSize(12);
                    eye1.makeVisible();
            
                  Circle eye2 = new Circle();
                    eye2.changeColor("eyeOne");
                    eye2.setX(310);
                    eye2.setY(230);
                    eye2.changeSize(12);
                    eye2.makeVisible();
            
                  //eye highlights
                  Circle eye3 = new Circle();
                    eye3.changeColor("eyeTwo");
                    eye3.setX(254);
                    eye3.setY(232);
                    eye3.changeSize(6);
                    eye3.makeVisible();
            
                  Circle eye4 = new Circle();
                    eye4.changeColor("eyeTwo");
                    eye4.setX(314);
                    eye4.setY(232);
                    eye4.changeSize(6);
                    eye4.makeVisible();
            
                  //ears
                    Ellipse ear = new Ellipse (20,30);
                    ear.setX(220);
                    ear.setY(200);
                    ear.changeColor("black");
                    ear.rotate(-10);
                    ear.makeVisible();
                  
                    Ellipse ears = new Ellipse (20,30);
                    ears.setX(335);
                    ears.setY(200);
                    ears.changeColor("black");
                    ears.rotate(10);
                    ears.makeVisible();
            
            
                  //nose
                  Ellipse nose = new Ellipse (15,25);
                    nose.setX(275);
                    nose.setY(238);
                    nose.changeColor("black");
                    nose.rotate(90);
                    nose.makeVisible();
            //mouth
                  Rect mouth = new Rect();
                    mouth.changeColor("black");
                    mouth.changeSize(3, 10);
                    mouth.setX(278);
                    mouth.setY(260);
                    mouth.rotate(88);
                    mouth.makeVisible();
            
                 //brown fur variations
            
                  Ellipse light = new Ellipse (100,40);
                    light.setX(220);
                    light.setY(310);
                    light.changeColor("brownOne");
                    light.rotate(20);
                    light.makeVisible();
                  
                    Ellipse base = new Ellipse (80,30);
                    base.setX(230);
                    base.setY(310);
                    base.changeColor("brownTwo");
                    base.rotate(20);
                    base.makeVisible();
            
            //brown second
                  Ellipse third = new Ellipse (90,30);
                    third.setX(200);
                    third.setY(410);
                    third.changeColor("brownOne");
                    third.rotate(20);
                    third.makeVisible();
                  
                    Ellipse fourth = new Ellipse (70,20);
                    fourth.setX(210);
                    fourth.setY(410);
                    fourth.changeColor("brownTwo");
                    fourth.rotate(20);
                    fourth.makeVisible();
            
                     
        //SECOND LEMUR BEGINS HERE
        
        
        
        //tail
        Rect tail = new Rect();
        tail.changeColor("black");
        tail.changeSize(40, 500);
        tail.setX(530);
        tail.setY(600);
        tail.rotate(90);
        tail.makeVisible();
        
                    //stripes begin :_(
                    Rect stripe = new Rect();
                    stripe.changeColor("white");
                    stripe.changeSize(40, 20);
                    stripe.setX(770);
                    stripe.setY(520);
                    stripe.rotate(90);
                    stripe.makeVisible();
                    
                    Rect stripe1 = new Rect();
                    stripe1.changeColor("white");
                    stripe1.changeSize(40, 20);
                    stripe1.setX(770);
                    stripe1.setY(560);
                    stripe1.rotate(90);
                    stripe1.makeVisible();
                    
                    Rect stripe2 = new Rect();
                    stripe2.changeColor("white");
                    stripe2.changeSize(40, 20);
                    stripe2.setX(770);
                    stripe2.setY(600);
                    stripe2.rotate(90);
                    stripe2.makeVisible();
                    
                    Rect stripe3 = new Rect();
                    stripe3.changeColor("white");
                    stripe3.changeSize(40, 20);
                    stripe3.setX(770);
                    stripe3.setY(640);
                    stripe3.rotate(90);
                    stripe3.makeVisible();
                    
                    Rect stripe4 = new Rect();
                    stripe4.changeColor("white");
                    stripe4.changeSize(40, 20);
                    stripe4.setX(770);
                    stripe4.setY(680);
                    stripe4.rotate(90);
                    stripe4.makeVisible();
                    
                    Rect stripe5 = new Rect();
                    stripe5.changeColor("white");
                    stripe5.changeSize(40, 20);
                    stripe5.setX(770);
                    stripe5.setY(720);
                    stripe5.rotate(90);
                    stripe5.makeVisible();
                    
                    Rect stripe6 = new Rect();
                    stripe6.changeColor("white");
                    stripe6.changeSize(40, 20);
                    stripe6.setX(770);
                    stripe6.setY(760);
                    stripe6.rotate(90);
                    stripe6.makeVisible();
                    
                    Rect stripe7 = new Rect();
                    stripe7.changeColor("white");
                    stripe7.changeSize(40, 20);
                    stripe7.setX(770);
                    stripe7.setY(800);
                    stripe7.rotate(90);
                    stripe7.makeVisible();
                    
                    Rect stripe8 = new Rect();
                    stripe8.changeColor("white");
                    stripe8.changeSize(40, 20);
                    stripe8.setX(770);
                    stripe8.setY(840);
                    stripe8.rotate(90);
                    stripe8.makeVisible();
                    
        
         //body
      Ellipse body2 = new Ellipse (270,160);
        body2.setX(600);
        body2.setY(310);
        body2.changeColor("gray");
        body2.rotate(50);
        body2.makeVisible();
        
        //belly
    Ellipse body3 = new Ellipse (200,90);
        body3.setX(630);
        body3.setY(370);
        body3.changeColor("offWhite");
        body3.rotate(50);
        body3.makeVisible();
        
        
        
    //trunk
    Rect trunk2 = new Rect();
        trunk2.changeColor("trunks");
        trunk2.changeSize(100, 1400);
        trunk2.setX(-200);
        trunk2.setY(550);
        trunk2.rotate(-25);
        trunk2.makeVisible();
        //end of backing
    
        //face left
    Ellipse face1 = new Ellipse (110,60);
        face1.setX(590);
        face1.setY(250);
        face1.changeColor("offWhite");
        face1.rotate(60);
        face1.makeVisible();
        
        //right
    Ellipse face2 = new Ellipse (110,60);
        face2.setX(630);
        face2.setY(250);
        face2.changeColor("offWhite");
        face2.rotate(-60);
        face2.makeVisible();
       
        //top of head
    Ellipse face3 = new Ellipse (117,40);
        face3.setX(606);
        face3.setY(240);
        face3.changeColor("gray");
        face3.rotate(0);
        face3.makeVisible();
        
                    
                    //eye surrounding
                    Ellipse eyepatch = new Ellipse (20,45);
                    eyepatch.setX(625);
                    eyepatch.setY(270);
                    eyepatch.changeColor("darkGray");
                    eyepatch.rotate(-20);
                    eyepatch.makeVisible();
                  
                    Ellipse eyepatch2 = new Ellipse (20,45);
                    eyepatch2.setX(675);
                    eyepatch2.setY(270);
                    eyepatch2.changeColor("darkGray");
                    eyepatch2.rotate(20);
                    eyepatch2.makeVisible();
        
                    
                //snout
                Ellipse noses = new Ellipse (40,30);
                noses.setX(640);
                noses.setY(300);
                noses.changeColor("darkGray");
                noses.makeVisible();

                Ellipse noses1 = new Ellipse (25,18);
                noses1.setX(647);
                noses1.setY(310);
                noses1.changeColor("black");
                noses1.makeVisible();
                
                //eyes begin
                    Circle eye11 = new Circle();
                    eye11.changeColor("eyeOne");
                    eye11.setX(630);
                    eye11.setY(290);
                    eye11.changeSize(12);
                    eye11.makeVisible();
            
                  Circle eye22 = new Circle();
                    eye22.changeColor("eyeOne");
                    eye22.setX(677);
                    eye22.setY(290);
                    eye22.changeSize(12);
                    eye22.makeVisible();
            
                  //eye highlights
                  Circle eye33 = new Circle();
                    eye33.changeColor("eyeTwo");
                    eye33.setX(634);
                    eye33.setY(292);
                    eye33.changeSize(6);
                    eye33.makeVisible();
            
                  Circle eye44 = new Circle();
                    eye44.changeColor("eyeTwo");
                    eye44.setX(681);
                    eye44.setY(292);
                    eye44.changeSize(6);
                    eye44.makeVisible();
            
                    
        //arms again
        //arms
        Ellipse arm1 = new Ellipse (150,30);
        arm1.setX(566);
        arm1.setY(415);
        arm1.changeColor("gray");
        arm1.rotate(100);
        arm1.makeVisible();
                  
        Ellipse arms1 = new Ellipse (150,30);
        arms1.setX(650);
        arms1.setY(390);
        arms1.changeColor("gray");
        arms1.rotate(110);
        arms1.makeVisible();
        
        Ellipse interior = new Ellipse (130,15);
        interior.setX(583);
        interior.setY(406);
        interior.changeColor("offWhite");
        interior.rotate(100);
        interior.makeVisible();
    
    }
}