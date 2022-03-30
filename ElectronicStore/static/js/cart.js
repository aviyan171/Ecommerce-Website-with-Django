// let addToCart=document.getElementById("btn")

// addToCart.addEventListener('click',()=>{
//     console.log('clicked')
// })


const increaseBtn=document.getElementById("increase")
const tquantity=document.getElementById("quantity1")
increaseBtn.addEventListener('click',()=>{
    id= increaseBtn.getAttribute('pid')
    // console.log(id)
    $.ajax({
        type:"GET",
        url:'/pluscart',
        data: {
            prod_id : id
        },
        success:(data)=>{
            tquantity.innerText=data.quantity
            
        }
    })
    
})

// const decreaseBtn=document.getElementById("decrease")

// $('#increase').click(()=>{
//     const id=$(this).attr("pid").toString()
//     $.ajax({
//         type:"GET",
//         url:'/pluscart',
//         data:{
//             prod_id=id
//         },
//     })
// })

