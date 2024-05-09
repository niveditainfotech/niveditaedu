function sidebar(){
    const bar = document.querySelector(".side-bar");
    bar.style.display='flex'
}

function show(){
    const bar = document.querySelector(".side-bar");
    bar.style.display='none'
    bar.style.transition='.5s'
}