<template>
    <!-- Footer -->
    <MDBFooter :text="['center', 'lg-start', 'muted']">
      <!-- Section: Social media -->
      <section class="
          d-flex
          justify-content-center justify-content-lg-between
          p-4
          border-bottom
        ">
        <!-- Left -->
        <div class="me-5 d-none d-lg-block">
          <span>Get connected with us on social networks:</span>
        </div>
        <!-- Left -->
        <!-- Right -->
        <div>
          <a href="" class="me-4 text-reset">
            <MDBIcon iconStyle="fab" icon="facebook-f"></MDBIcon>
          </a>
          <a href="" class="me-4 text-reset">
            <MDBIcon iconStyle="fab" icon="twitter"></MDBIcon>
          </a>
          <a href="" class="me-4 text-reset">
            <MDBIcon iconStyle="fab" icon="google"></MDBIcon>
          </a>
          <a href="" class="me-4 text-reset">
            <MDBIcon iconStyle="fab" icon="instagram"></MDBIcon>
          </a>
          <a href="" class="me-4 text-reset">
            <MDBIcon iconStyle="fab" icon="linkedin"></MDBIcon>
          </a>
          <a href="" class="me-4 text-reset">
            <MDBIcon iconStyle="fab" icon="github"></MDBIcon>
          </a>
        </div>
        <!-- Right -->
      </section>
      <!-- Section: Social media -->
      <!-- Section: Links  -->
      <section class="">
            <MDBCol md="3" lg="4" xl="3" class="mx-auto mb-4">
              <!-- Content -->
              <h6 class="text-uppercase fw-bold mb-4">
                <i class="fas fa-gem me-3"></i>Tooth Hub
              </h6>
            </MDBCol>
            <!-- Grid column -->
            <!-- Grid column -->
            <MDBCol md="4" lg="3" xl="3" class="mx-auto mb-md-0 mb-4">
              <!-- Links -->
              <h6 class="text-uppercase fw-bold mb-4">Contact</h6>
              <p>
                <i class="fas fa-home me-3"></i> New York, NY 10012, US
              </p>
              <p>
                <i class="fas fa-envelope me-3"></i>
                info@example.com
              </p>
              <p>
                <MDBIcon icon="phone" class="me-3" /> + 01 234 567 88
              </p>
              <p>
                <MDBIcon icon="print" class="me-3" /> + 01 234 567 89
              </p>
            </MDBCol>
      </section>
    </MDBFooter>
    <!-- Footer -->
  </template>
  <script>
  import {
    MDBFooter,
    MDBCol,
    MDBIcon
  } from 'mdb-vue-ui-kit';

  export default {
    components: {
      MDBFooter,
      MDBCol,
      MDBIcon
    },
  };
</script>