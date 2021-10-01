<p>安装nightmare</p>
<p>编写1.js</p>
<p>运行 node 1.js</p>
<p>var Nightmare = require('nightmare');<br />var nightmare = Nightmare({ show: true })</p>
<p>nightmare<br />  .goto('http://yahoo.com')<br />  .type('form[action*="/search"] [name=p]', 'github nightmare')<br />  .click('form[action*="/search"] [type=submit]')<br />  .wait('#main')<br />  .evaluate(function () {<br />    return document.querySelector('#main .searchCenterMiddle li a').href<br />  })<br />  .end()<br />  .then(function (result) {<br />    console.log(result)<br />  })<br />  .catch(function (error) {<br />    console.error('Search failed:', error);<br />  });</p>