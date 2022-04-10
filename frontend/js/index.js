$(document).ready(function() {
    jQuery.support.cors = true;
    get_latest_products();
    get_products_by_type(1, '#fresh_products');
    get_products_by_type(2, '#fruits_products');
});

function get_products_by_type(t, target) {
    $.ajax({
        url: 'http://localhost:6868/food-blog/api/product?type=' + t + '&size=6',
        crossDomain : true,
        dataType : "jsonp",
        type: 'GET',
        jsonp: "callback",
        contentType: "application/json; charset=utf-8",
        success: function(data, state, res){
            if (data == null) { return; };
            var items = [];
            $.each(data, function(index, item) {
                items.push(reder_type_products(item, index));
            });
            $(target).append(items.join(""));
        }
    });
}

function reder_type_products(item, idx) {
    console.log(item, idx);
    var htmlText = idx < 3 ? '<div class="col-md-4 col-sm-4 col-lg-4 col-xs-12">' : '<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">';
    htmlText += idx < 3 ? '<div class="product-thumb">' : '<div class="product-thumb1">';
    htmlText += '<div class="image">';
    htmlText += '<a href="shop.html">';
    htmlText += "<img src='http://localhost:6868/static/" + (idx < 3 ? item['Image'] : item['DealImage']) + "' alt='image' title='image' class='img-fluid'>";
    htmlText += '</a>';
    if (idx < 3) {
        htmlText += '<div class="onhover1">';
        htmlText += '<div class="button-group">';
        htmlText += '<button class="btn-icon" type="button"><i class="icon_piechart"></i></button>';
        htmlText += '<button class="icons" type="button"><i class="icon_cart_alt"></i></button>';
        htmlText += '<button class="btn-icon" type="button"><i class="icon_heart_alt"></i></button>';
        htmlText += '</div>';
        htmlText += '</div>';
    }
    htmlText += '</div>';
    htmlText += idx < 3 ? '<div class="caption text-center">' : '<div class="caption">';
    htmlText += idx < 3 ? '<h4><a href="shop.html">' + item['Name'] + '</a></h4>' : '<h4>' + item['Name'] + '</h4>';
    
    if (idx < 3) {
        htmlText += '<div class="rating">';
        for (var i = 1; i < 5; i++) {
            htmlText += (i == item['Vote']) ? "<i class='fa fa-star-o'></i>" : "<i class='fa fa-star'></i>";
        }
        htmlText += '</div>';

        
        htmlText += (item['OldPrice']) && (item['OldPrice'] > 0) ? "<p class='price'><span>$" + item['OldPrice'] + "</span> $" : "<p class='price'>$";
        htmlText += item['Price']  + "</p>";
    } else {
        htmlText += '<p>Price : <span>$' + item['Price'] + '</span></p>';
        htmlText += '<div class="button-group"><button type="button"><i class="icon_cart_alt"></i></button><button type="button"><i class="icon_heart_alt"></i></button></div>'
    }
    htmlText += '</div></div></div>';
    return htmlText;
}

function get_latest_products() {
    $.ajax({
        url: 'http://localhost:6868/food-blog/api/product?latest=1&size=8',
        crossDomain : true,
        dataType : "jsonp",
        type: 'GET',
        jsonp: "callback",
        contentType: "application/json; charset=utf-8",
        success: function(data, state, res){
            if (data == null) { return; };
            var items = [];
            $.each(data, function(index, item) {
                items.push(reder_latest_products(item));
            });
            $("#lastest_products").append(items.join(""));
        }
    });
}


function reder_latest_products(item) {
    var htmlText = "<div class='col-md-3 col-lg-3 col-sm-4 col-xs-12'>";
    htmlText += "<div class='product-thumb'>";
    htmlText += "<div class='image'>";
    htmlText += "<a href='shop.html'>";
    htmlText += "<img src='http://localhost:6868/static/" + item['Image'] + "' alt='image' title='image' class='img-fluid'>";
    htmlText += "</a>";
    htmlText += "<div class='onhover1'><div class='button-group'>";
    htmlText += "<button class='btn-icon' type='button'><i class='icon_piechart'></i></button>";
    htmlText += "<button class='icons' type='button'><i class='icon_cart_alt'></i></button>";
    htmlText += "<button class='btn-icon' type='button'><i class='icon_heart_alt'></i></button></div></div></div>";
    htmlText += "<div class='caption text-center'>";
    htmlText += "<h4><a href='shop.html'>" + item['Name'] + "</a></h4>";
    htmlText += "<div class='rating'>";
    for (var i = 1; i < 5; i++) {
        htmlText += (i == item['Vote']) ? "<i class='fa fa-star-o'></i>" : "<i class='fa fa-star'></i>";
    }
    htmlText += "</div>";
    htmlText += (item['OldPrice']) && (item['OldPrice'] > 0) ? "<p class='price'><span>$" + item['OldPrice'] + "</span> $" : "<p class='price'>$";
    htmlText += item['Price']  + "</p>";
    htmlText += "</div></div></div>";
    return htmlText;
};
