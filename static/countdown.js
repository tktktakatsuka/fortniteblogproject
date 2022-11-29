"use strict";

function countdown(due) {
  /* コメントの書き方*/
  /* constは定数*/
  const now = new Date();
  const rest = due.getTime() - now.getTime();
  const sec = Math.floor(rest / 1000) % 60;
  const min = Math.floor(rest / 1000 / 60) % 60;
  const hours = Math.floor(rest / 1000 / 60 / 60) % 24;
  const days = Math.floor(rest / 1000 / 60 / 60/ 24) ;
  const count = [days ,hours, min, sec];
  return count;
}

/* 残り時間を画面に表示する関数  */
function recalc() {
  console.log(countdown(goal));
  const counter = countdown(goal);
  const time = `${counter[0]}日${counter[1]}時間${counter[2]}分${counter[3]}秒`;
  console.log(time);
  document.getElementById("timer").textContent = time;

  refresh();
}

/* 1秒ごとにリフレッシュする関数を定義*/
function refresh(){
    setTimeout(recalc, 1000);
}


/* main処理 */
/* letは変数*/
let goal = new Date( 2022, 11, 4 , 6);
console.log(goal)

/* 終わりの時間をセッティングする。*/


recalc();

