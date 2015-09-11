/**
 * Created by Maxwell J. Resnick on 9/1/15.
 */

// Overkill for this assignment - init jQuery as $jQ
var $jQ = jQuery.noConflict();

function javapicImages (cssBackground) {
       /*
        * javapicImages
        * @description urls for random bg images and galleries.
        * @returns radomImage [array] 6 image file paths
        * @returns allImages [array] 60 image paths.
        * Using an IIFY for fun but also we only need this list once, per page load.
        */
        this.cssBackground = cssBackground;
        var filePrefix = (this.cssBackground ? "url(static/images/pdxcg_" : "static/images/pdxcg_");
        var filePostfix = (this.cssBackground ? ".jpg)" : ".jpg");
        this.randomImages = (
            function () {
            var _randomImages = [];
            for (var i = 0; i < 7; i++) {
                // we go up to 60, but add 1 in the end to account for 0.
                var num = Math.floor(Math.random() * 60) + 1;
                // we add a "0" but also just cast everything to string
                if (num < 10) {
                    num = "0" + num.toString();
                } else {
                    num = num.toString();
                }
                var fullPath = filePrefix + num + filePostfix;
                _randomImages.push(fullPath);
            }
            return _randomImages;
        }());
        this.allImages = (
            function() {
            var images = [];
            for (var i = 0; i < 60; i++) {
                var num = i+1;
                // we add a "0" but also just cast everything to string
                if (num < 10) {
                    num = "0" + num.toString();
                } else {
                    num = num.toString();
                }
                var fullPath = filePrefix + num + filePostfix;
                images.push(fullPath);
                }
                return images;
        }());
}


