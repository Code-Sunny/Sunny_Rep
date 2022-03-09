

let temp_html = `<div class="card" style="width: 18rem;">
                    <img src="..." class="card-img-top" alt="...">
                    <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>`


$(document).ready(function() {
    show_content();
});

function show_content() {
    $.ajax({
        type: "GET",
        url: "/show",
        data: {},
        success: function (response) {
            console.log(response)
            infos = response['all_contents'];
            for (let i =0; i<infos.length; i++) {
                console.log(infos[i])
                let name = infos[i][0]
                let title = infos[i][1]
                let img = infos[i][2]
                let pre_here = infos[i][3]

                let temp_html = `<div class="card" style="width: 18rem;">
                    <img src="${img}" class="card-img-top" alt="...">
                    <div class="card-body">
                    <h5 class="card-title">${name}</h5>
                    <p class="card-text">title : <span style=" font: bold 1.1em/1em Georgia, serif ;">${title}</span></p>
                    <a href="${pre_here}" class="btn btn-primary">미리 듣기</a>
                    </div>
                </div>`

                $('#contents').append(temp_html)
            }
            // let reviews = response['all_orders'];
            // for(let i =0; i<reviews.length; i++) {
            //     let name = reviews[i]['name'];
            //     let quantity = reviews[i]['quantity'];
            //     let adress = reviews[i]['adress'];
            //     let phoneNumber = reviews[i]['phoneNumber'];

            //     console.log(name, quantity, adress, phoneNumber);

            //     let temp_html = `<tr>
            //                         <td>${name}</td>
            //                         <td>${quantity}</td>
            //                         <td>${adress}</td>
            //                         <td>${phoneNumber}</td>
            //                     </tr>`
            //     $('#order-box').append(temp_html)
            //     console.log(temp_html)
        }
    })
}



// function order(){
//     // 서버에서 요구하는 데이터를 보내줍시다. 형식은 JSON 이욤!
//         let name = $('#name').val();
//         let quantity = $('#inputGroupSelect01').val();
//         let adress = $('#adress').val();
//         let phoneNumber = $('#phoneNumber').val();

//         $.ajax({
//             type: "POST",
//             url: "/review",
//             data: {
//                 name_give:name, quantity_give:quantity, adress_give:adress, phoneNumber_give:phoneNumber
//             },
//             // 서버에서는 데이터를 뭘로 받기로 했을까요?
//             success: function (response) {
//                 alert(response["msg"]);
//                 window.location.reload();
//             }
//         })
//     alert('주문이 완료되었습니다!');
// }

// // 환율을 새로고침 할 때마다 표시하는 부분, url은 app.py와 무관하게 별도로 url에서 데이터를 받아와 독자적으로 처리함.
// $.ajax({
//     type: "GET",
//     url: "http://spartacodingclub.shop/sparta_api/rate",
//     data: {},
//     success: function (response) {
//         let rate = response["rate"]
//         $(document).ready(function () {
//             $('#exchange_rate').text(`달러-원 환율 : ${rate}`)
//         });
//     }
// })


