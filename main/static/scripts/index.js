$(document).ready(function () {
  $(".swiper").slick({
    dots: false,
    infinite: true,
    adaptiveHeight: true,
    autoplay: true,
    arrows: false,
  });
  $(".cert").lightGallery();
});

$("#catalog").click(toggleDropdown);
$(".nav--nested").click(toggleDropdownContent);

function toggleDropdown() {
  if ($("#catalog-dropdown").is(":hidden")) {
    $("#catalog-dropdown").slideDown("fast");
  } else {
    $("#catalog-dropdown").slideUp("fast");
  }
}

function toggleDropdownContent() {
  let selector = "#" + $(this).attr("data-dropdown");
  if ($(selector).is(":hidden")) {
    $(selector).slideDown("fast");
  } else {
    $(selector).slideUp("fast");
  }
}
