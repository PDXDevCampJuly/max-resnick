/**
 * Created by Maxwell J. Resnick on 9/3/15.
 */
var $jQ = new jQuery.noConflict();

function processData(data) {
    var $ourData = $jQ(data);
    $ourData.find('item').each(
        function () {
            var $newItem = $jQ(this);
            products.push(new Product($newItem.attr('name'),
                                $newItem.attr('price'),
                                $newItem.children('numInStock').text()));
        }
    );
    // Init Material & Add initialized row.
    populateInventory();
}

(function () {
    /*
     * @description loads an xml file.
     */
    $jQ.ajax({
            type: "GET",
            url: "data/inventory.xml",
            success: function (data) {
                processData(data);
            },
            statusCode: {
                404: function () {
                    $jQ('table').before("<h3> An error occured, we can't provide materials at this time.</h3>")
                    $jQ('h3').css("color", "tomato");
                },
            },
        });
}());