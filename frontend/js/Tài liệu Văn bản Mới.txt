function generateColorforShop =()=>{
    let color;
    let r=Math.floor(Math.random()*256);
    let g=Math.floor(Math.random()*256);
    let b=Math.floor(Math.random()*256);
    color=`rgb(${r} ,${g} ,${b})`
    dropdown-toggle.style.color=color
}
setInterval(generateColorforShop,1000)