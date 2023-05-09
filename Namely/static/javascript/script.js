var days=new Date
     
var d=days.getDate();

var m=days.getMonth();
var y=days.getFullYear();
var n=days.getDay();
var dayss=['Sunday','Monday','Tuesday','Thursday','Friday','Saturday']
var datetime= dayss[n]+" "+d+" /"+m+"/ "+y
console.log(datetime);
var time=days.getHours();

document.getElementById('dateandtime').innerHTML=datetime

var txt;
if(time>=12&&time<18){
// document.getElementById('target1').innerHTML=  g;
  txt= "USER"+"   "+"GOOD AFTERNOON";
}else if(time>=18&&time<=20){
  txt='USER'+" "+"GOOD EVENING";
}
else if(time>=21&&time<=24){
  txt='USER'+" "+"GOOD NIGHT";
}
else{
  txt='USER'+" "+"GOOD MORNING";
}


var txt1= "REMOVE YOURSELF";
var i=0;
var speed=300;
fun(i,txt,speed)

function fun() {
 
  if (i < txt.length) {
    document.getElementById("target").innerHTML += txt.charAt(i);
    i++;
    setTimeout(fun, speed);
    
  } 
 
  setTimeout(fun, speed);

}




