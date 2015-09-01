/*
 * Javapic utilizing Jquery
 */


// Overkill for this assignment
var $jQ = jQuery.noConflict();
$jQ(document).ready(function(){

    var rotatorImages = (function () {
   /*
    * rotatorImages
    * @description  First we need to select some images of the 60
    * @returns [array] 6 image file paths
    * Using an IIFY for fun but also we only need this list once, per page load.
    */
    this.randomImages = [];
    for (var i=0; i<7; i++) {
        this.filePrefix = "images/pdxcg_";
        this.filePostfix= ".jpg";
        // we go up to 60, but add 1 in the end to account for 0.
        this.num = Math.floor(Math.random()*60) + 1;

        // we add a "0" but also just cast everything to string
        if (this.num < 10) {
            this.num = "0" + this.num.toString();
        } else {
            this.num = this.num.toString();
        }
        this.fullPath = this.filePrefix + this.num + this.filePostfix;
        this.randomImages.push(this.fullPath);
    }
    return this.randomImages;
}());
});
