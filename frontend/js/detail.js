$(document).ready(function() {
    jQuery.support.cors = true;
    const urlParams = new URLSearchParams(window.location.search);
    const product_id = urlParams.get('id');
    get_product(product_id);
});


function get_product(product_id) {
    $.ajax({
        url: 'http://localhost:6868/food-blog/api/product?id=' + product_id,
        crossDomain : true,
        dataType : "jsonp",
        type: 'GET',
        jsonp: "callback",
        contentType: "application/json; charset=utf-8",
        success: function(data, state, res){
            if (data == null) { return; };
            reder_product(data[0]);
        }
    });
}

function reder_product(item) {
    console.log(item);
    $('#product_name').empty().append(item['Name']);
    $('#shot_des').empty().append(item['Description']);
    if (item['NotChemical'] == 1) {
        $('#is_chemicals').empty().append('<i class="icon_box-checked"></i> 100% Fresh not Chemicals');
    } else {
        $('#is_chemicals').empty().append('<i class="icon_box-empty"></i> 100% Fresh not Chemicals');
    }
    if (item['FromFarm'] == 1) {
        $('#is_from_fram').empty().append('<i class="icon_box-checked"></i> 100% Fresh Food from farm');
    } else {
        $('#is_from_fram').empty().append('<i class="icon_box-empty"></i> 100% Fresh Food from farm');
    }
    if (item['Organic'] == 1) {
        $('#is_organic').empty().append('<i class="icon_box-checked"></i> 100% Organic food');
    } else {
        $('#is_organic').empty().append('<i class="icon_box-empty"></i> 100% Organic food');
    }
    $('#price').empty().append('$ ' + item['Price']);
    $('#big_image1').empty().append('<img src="http://localhost:6868/static/' + item['BigImage1'] + '" title="img" alt="img" />');
    $('#small_image1').empty().append('<img src="http://localhost:6868/static/' + item['SmallImage1'] + '" title="img" alt="img" />');
    $('#small_image2').empty().append('<img src="http://localhost:6868/static/' + item['SmallImage2'] + '" title="img" alt="img" />');

    htmlText = '';
    for (var i = 0; i < 5; i++) {
        htmlText += ((i + 1) > item['Vote']) ? "<i class='fa fa-star fa-star-l'></i>" : "<i class='fa fa-star'></i>";
    }
    $('#rating').empty().append(htmlText);
}