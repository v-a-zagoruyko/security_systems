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
$("#catalog-m").click(toggleMobileDropdown);
$(".toggle").click(toggleMenu);
$(".nav--nested").click(toggleDropdownContent);

function toggleDropdown() {
  if ($("#catalog-dropdown").is(":hidden")) {
    $("#catalog-dropdown").slideDown("fast");
  } else {
    $("#catalog-dropdown").slideUp("fast");
  }
}

function toggleMobileDropdown() {
  if ($("#catalog-m-dropdown").is(":hidden")) {
    $("#catalog-m-dropdown").slideDown("fast");
  } else {
    $("#catalog-m-dropdown").slideUp("fast");
  }
}

function toggleMenu() {
  if ($("#menu-nav-mobile").is(":hidden")) {
    $("#menu-nav-mobile").slideDown("fast");
  } else {
    $("#menu-nav-mobile").slideUp("fast");
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
