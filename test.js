function menuGlobal() {
    console.log("오늘 저녁은 " + this.name);
}

var myDiner = {
    name: "김치찌개",
    menu: menuGlobal
}
myDiner.menu();


var yourDiner = {
    name: "된장찌개",
    menu: menuGlobal
}
yourDiner.menu();
