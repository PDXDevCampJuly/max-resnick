/**
 * Created by Maxwell J. Resnick on 9/2/15.
 */
var imageArray = new javapicImages(false).allImages;
var $modal = $jQ('#image_show');

function displayModal($target) {
    /*
     * @description displays modal of clicked image.
     */
    $modal.children().replaceWith($target.clone());
    // Meglo chain
    $modal.toggleClass('display_none', false).toggleClass('display_img')
        .on("click", function (e) {
            if ($jQ(e.target).is($modal)) {
                $modal.toggleClass('display_img', false).toggleClass('display_none').off();
            };
        });
}
(function (){
    /*
     * @description "paint" html all over the place w/ out images.
     */
    // <li><img src="images/pdxcg_01.jpg" /></li>
    var $section = $jQ('#gallery');
    for (var i=0; i<imageArray.length; i++) {
        this.newImage = '<li><img src="' + imageArray[i] + '" /></li>';
        $section.append(this.newImage);

    }
}());

(function (){
    /*
     * @description we set our username if logged in and forget it.
     */
    var username = sessionStorage.getItem('javapic');
    if (username !== null || username !== undefined) {
        newName = $jQ('.tagline');
        newName.text(newName.text().replace("tiffany", username));
    } else {
        location.href = "join.html";
    }
}());

// Event Binding

$jQ("#gallery").on("click","img", function(e){
        displayModal($jQ(e.target));
    }
);
