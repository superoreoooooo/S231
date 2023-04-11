import React, { useState } from 'react';
import './App.css';

function App() {
  let style = {color : 'white', fontSize : '30px'}

  var[titles, changeTitles] = useState(["아침 뭐먹지", "점심 뭐먹지", "저녁 뭐먹지", "야식 뭐먹지"]);
  var[dates, changeDates] = useState(["4월 11일", "4월 12일", "4월 13일", "4월 14일"])

  var[t, ct] = useState(0);

  function changeTitle() {
    var arr = [...titles];
    arr[0] = "아침 안먹어야지";
    changeTitles(arr);
  }

  return (
    <div className="App">

      <div className="black-nav">
        <div style={ style }>개발 blog</div>
      </div>

      <button onClick={ changeTitle }>버튼</button>

      <div className="list">
        <h3> { titles[0] } <span onClick={() => { ct(t + 1) }}>👍</span> { t } </h3>
        <p> { dates[0] } </p>
        <hr/>
      </div>

      <div className="list">
        <h3> { titles[1] } </h3>
        <p> { dates[1] } </p>
        <hr/>
      </div>

      <div className="list">
        <h3> { titles[2] } </h3>
        <p> { dates[2] } </p>
        <hr/>
      </div>

      <div className="list">
        <h3> { titles[3] } </h3>
        <p> { dates[3] } </p>
        <hr/>
      </div>

      <Modal/>

    </div>
  );
}

function Modal() {
  return (
    <div className='modal'>
      <h2>title</h2>
      <p>date</p>
      <p>data</p>
    </div>
  )
}

export default App;
