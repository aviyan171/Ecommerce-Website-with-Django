

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

$("#addForm").submit(function(e){
  
    $.ajax({
      data:$(this).serialize(),
      method:$(this).attr('method'),
      url:$(this).attr('action'),
      dataType:'json',
      success:function(res){
        if(res.bool==true){

            $(".ajaxRes").html('Data has been added.')
            $("#reset").trigger('click')
            $(".reviewBtn").hide()

            let _html='<div class="reviewlist">'
            _html+='<span>Avg reviews:'+ res.avg_reviwes.avg_rating.toFixed(1)+'/5</span> '
             _html+='<blockquote>'
            _html+='<small>'+res.data.review_text+'</small>'
            _html+='<br>'
            for (let i=1; i<=res.data.review_rating;i++){
            _html+='<span class="fa fa-star checked"></span>'
           }
           _html+='</blockquote>'
           _html+='<span> Reviewed by:' +res.data.user+'</span>'
           _html+='</div>'

           $(".reviewlist").prepend(_html)
           $('#productReview').modal('hide')
           $('.Avg-rating').text(res.avg_reviwes.avg_rating.toFixed(1))
        }
      }
    })
    e.preventDefault()
  })
  


