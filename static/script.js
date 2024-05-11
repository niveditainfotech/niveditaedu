function sidebar(){
    const bar = document.querySelector(".side-bar");
    bar.style.display='flex'
}

function show(){
    const bar = document.querySelector(".side-bar");
    bar.style.display='none'
    bar.style.transition='.5s'
    console.log("Test")
}

console.log("Test");

let preloader=document.querySelector("[data-preaload]")

window.addEventListener("load",loader)

function loader(){
    preloader.classList.add("loaded")
    document.body.classList.add("loaded")
}

