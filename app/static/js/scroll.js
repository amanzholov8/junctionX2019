var active = false;
currentPos = 1;

function scroll() {
    while (active) {
        currentPos += 1;
        $('html, body').animate({
            scrollTop: $(`#div${currentPos}`).offset().top
        }, 4000);        
        console.log(active);
        delay(400);
    };
};

$(document).on("click", function () {            
    console.log("received click");
    debugger;
    if (active) {
        active = false;
        console.log(`active after setting to false ${active}`);
    }
    console.log("after if loop");
});

$("#play").on("click", function () {
    active = true;
    scroll();
});