/**
 * Created by Maxwell J. Resnick on 9/3/15.
 */
var $jQ = new jQuery.noConflict();

function processJSONData (data) {
    if ("item" in data.inventory) {
        $jQ.each(data.inventory.item, function () {
            var $newItem = this;
            products.push(new Product($newItem.name,
                                      $newItem.price,
                                      $newItem.numInStock));
            });
        populateInventory();
    }
}


function processXMLData(data) {
    var $ourData = $jQ(data);
    $ourData.find('item').each(
        function () {
            var $newItem = $jQ(this);
            products.push(new Product($newItem.attr('name'),
                                $newItem.attr('price'),
                                $newItem.children('numInStock').text()));
        }
    );
    // Init Material
    populateInventory();
}

(function () {
    /*
     * @description loads the xml or json file.
     */
    var isJSON, fileURL;
    if (Math.random() < .5) {
        isJSON = true;
        fileURL = "data/inventory.json";
    } else {
        isJSON = false;
        fileURL = "data/inventory.xml";
    }
    $jQ.ajax({
            type: "GET",
            url: fileURL,
            success: function (data) {
                if (isJSON) {
                    processJSONData(data);
                } else {
                    processXMLData(data);
                }
            },
            statusCode: {
                404: function () {
                    $jQ('table').before("<h3> An error occured, we can't provide materials at this time.</h3>")
                    $jQ('h3').css("color", "tomato");
                },
            },
        });
}());