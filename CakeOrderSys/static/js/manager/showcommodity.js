$(document).ready(function () {
    /**
     *制作卡片实时显示*/
    //宣传图
    var myicon = $("input#primaryIcon")[0]
    var cardicon = $("img.card-img-top")[0]
    myicon.oninput = function () {
        if (myicon.value == "") {
            cardicon.src = "https://via.placeholder.com/700x400?text=April"
            return
        }
        cardicon.src = window.URL.createObjectURL(myicon.files[0])
    }
    //产品名
    var myinput = $("input#name")[0]
    var cardtitle = $("h5.card-title")[0]
    myinput.oninput = function () {
        if (myinput.value == "") {
            cardtitle.innerText = "产品名"
            return
        }
        cardtitle.innerText = myinput.value
    }
    //产品描述
    var mydetail = $("textarea#detail")[0]
    var carddetail = $("p.card-text")[0]
    
    mydetail.oninput = function () {
        if (mydetail.value == "") {
            carddetail.innerText = "产品名"
            return
        }
        carddetail.innerText = mydetail.value
    }
  });