
let startT = Date.now();

function tick() {
  let currentT = Date.now();
  let elapsed = Math.floor((currentT - startT) / 1000);
  let sec = String(elapsed % 60);       //padStart(a,b) 문자열 길이가 a가 될 때까지 문자열 앞을 b로 채움

  document.getElementById("timer_A").innerText = `${sec}`;
  document.getElementById("uTime_A").value = elapsed;
}

setInterval(tick, 1000);
