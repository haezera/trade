import React from "react";
import "./Donut.css";
import "./computer_pixel-7.ttf";

class Donut extends React.Component {
  render() {
    return (
      <div className="donut-frame">
        <button id="toggle-btn" onClick={this.handleClick}>
          DONUT PLEASE
        </button>
        <pre id="ascii">{`
             k;double sin()
         ,cos();main(){float A=
       0,B=0,i,j,z[1760];char b[
     1760];printf("\x1b[2J");for(;;
  ){memset(b,32,1760);memset(z,0,7040)
  ;for(j=0;6.28>j;j+=0.07)for(i=0;6.28
 >i;i+=0.02){float c=sin(i),d=cos(j),e=
 sin(A),f=sin(j),g=cos(A),h=d+2,D=1/(c*
 h*e+f*g+5),l=cos      (i),m=cos(B),n=s
in(B),t=c*h*g-f*        e;int x=40+30*D*
(l*h*m-t*n),y=            12+15*D*(l*h*n
+t*m),o=x+80*y,          N=8*((f*e-c*d*g
 )*m-c*d*e-f*g-l        *d*n);if(22>y&&
 y>0&&x>0&&80>x&&D>z[o]){z[o]=D;;;b[o]=
 ".,-~:;=!*#$@"[N>0?N:0];}}/*#****!!-*/
  printf("\x1b[H");for(k=0;1761>k;k++)
   putchar(k%80?b[k]:10);A+=0.04;B+=
     0.02;}}/*****####*******!!=;:~
       ~::==!!!**********!!!==::-
         .,~~;;;========;;;:~-.
             ..,--------,*/
             `}</pre>
      </div>
      // <button id='toggle-btn' onClick={this.handleClick}>DONUT PLEASE</button>
    );
  }
  handleClick() {
    var togglebtn = document.getElementById("toggle-btn");
    var pretag = document.getElementById("ascii");
    if (togglebtn.style.display !== "none") {
      togglebtn.style.display = "none";
      pretag.style.display = "block";
      pretag.style.color = "white";
    }
    spin();
  }
}

// Created by Andy Sloane. https://www.a1k0n.net/2011/07/20/donut-math.html
// Refactored to run in react.
function spin() {
  var pretag = document.getElementById("ascii");

  var tmr1 = undefined;
  var A = 1,
    B = 1;
  var i;

  // This is copied, pasted, reformatted, and ported directly from my original
  // donut.c code
  var asciiframe = function () {
    var b = [];
    var z = [];
    A += 0.07;
    B += 0.03;
    var cA = Math.cos(A),
      sA = Math.sin(A),
      cB = Math.cos(B),
      sB = Math.sin(B);
    for (var k = 0; k < 1760; k++) {
      b[k] = k % 80 === 79 ? "\n" : " ";
      z[k] = 0;
    }
    for (var j = 0; j < 6.28; j += 0.07) {
      // j <=> theta
      var ct = Math.cos(j),
        st = Math.sin(j);
      for (i = 0; i < 6.28; i += 0.02) {
        // i <=> phi
        var sp = Math.sin(i),
          cp = Math.cos(i),
          h = ct + 2, // R1 + R2*cos(theta)
          D = 1 / (sp * h * sA + st * cA + 5), // this is 1/z
          t = sp * h * cA - st * sA; // this is a clever factoring of some of the terms in x' and y'

        var x = 0 | (40 + 30 * D * (cp * h * cB - t * sB)),
          y = 0 | (12 + 15 * D * (cp * h * sB + t * cB)),
          o = x + 80 * y,
          N =
            0 |
            (8 *
              ((st * sA - sp * ct * cA) * cB -
                sp * ct * sA -
                st * cA -
                cp * ct * sB));
        if (y < 22 && y >= 0 && x >= 0 && x < 79 && D > z[o]) {
          z[o] = D;
          b[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];
        }
      }
    }
    pretag.innerHTML = b.join("");
  };

  if (tmr1 === undefined) {
    tmr1 = setInterval(asciiframe, 51);
  } else {
    clearInterval(tmr1);
    tmr1 = undefined;
  }
  asciiframe();
}

export default Donut;
