

$('.chg-quantity').click(function(){
    let id=$(this).attr("pid").toString();
    let eml=this.parentNode.children[3]
    console.log(eml)
    console.log(id)
    $.ajax({
              type:"GET",
               url:'/pluscart',
               data: {
                    prod_id : id
                },
                success:(data)=>{
                    eml.innerText=data.quantity
                    document.getElementById("amount").innerText=data.amount
                    document.getElementById("totalamount").innerText=data.totalprice

                }
})

})

$('.chg-quantity1').click(function(){
    let id=$(this).attr("pid").toString();
    let eml=this.parentNode.children[3]
    console.log(eml)
    console.log(id)
    $.ajax({
              type:"GET",
               url:'/minuscart',
               data: {
                    prod_id : id
                },
                success:(data)=>{
                    eml.innerText=data.quantity
                    document.getElementById("amount").innerText=data.amount
                    document.getElementById("totalamount").innerText=data.totalprice

                }
})

})

$('.product-remove').click(function(){
    let id=$(this).attr("pid").toString();
    var eml=this
    console.log(id)
    
    $.ajax({
              type:"GET",
               url:'/removecart',
               data: {
                    prod_id : id
                },
                success:function(data){
                    console.log("delete")
                    console.log(eml.parentElement.parentElement)
                    eml.parentElement.parentElement.remove()
                    
                    document.getElementById("amount").innerText=data.amount
                    document.getElementById("totalamount").innerText=data.totalprice
                }
})

})


// const increaseBtn=document.querySelector(".chg-quantity")
// const productinfo=document.querySelector(".product-info")
// let eml=productinfo.querySelector('.quantity1')

// increaseBtn.addEventListener('click',()=>{
//     id= increaseBtn.getAttribute('pid')
//     console.log(id)
//     $.ajax({
//         type:"GET",
//         url:'/pluscart',
//         data: {
//             prod_id : id
//         },
//         success:(data)=>{
//         //  console.log(data.quantity) 
//         //  console.log(data.totalprice) 
//          eml.innerText=data.quantity
//          document.getElementById("amount").innerText=data.amount
//          document.getElementById("totalamount").innerText=data.totalprice
        
//         }
//     })
    
// })

// const decreaseBtn=document.getElementById("decrease")

// decreaseBtn.addEventListener('click',()=>{
//     id= decreaseBtn.getAttribute('pid')
//     $.ajax({
//         type:"GET",
//         url:'/minuscart',
//         data: {
//             prod_id : id
//         },
//         success:(data)=>{
//         //  console.log(data.quantity) 
//         //  console.log(data.totalprice) 
//          eml.innerText=data.quantity
//          amount.innerText=data.amount
//          totalamount.innerText=data.totalprice
        
//         }
//     })
    
// })


// const remove=document.getElementById("prod-remove")

// remove.addEventListener('click',(e)=>{
//     // const btnclicked=e.target
//     // console.log(btnclicked)
//     // btnclicked.parentElement.parentElement.parentElement.parentElement
    
//     id= remove.getAttribute('pid')
//     console.log(id)
//     $.ajax({
//         type:"GET",
//         url:'/removecart',
//         data: {
//             prod_id : id
//         },
//         success:(data)=>{
//             console.log('delete')
//         //  console.log(data.quantity) 
//         //  console.log(data.totalprice) 
        
//         document.getElementById("amount").innerText=data.amount
//         document.getElementById("totalamount").innerText=data.totalprice
        
        
//         }
//     })
    
// })

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

