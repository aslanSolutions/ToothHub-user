<template>
  <div class="group">
    <div class="appointments">
      Today’s Appointments
    </div>

    <div class="group">
      <div class="image-text-container">
        <div class="ellipse" id="ellipse806"></div>

        <div class="text-info">
          <div class="name">
            Roisin Durham
          </div>

          <div class="email">
            RoisinDurham@gmail.com
          </div>

          <div class="time">
            13:00 PM
          </div>

          <div class="dental-implant">
            Dental Implant
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style lang="scss">



.appointments {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-size:20px;
  line-height: 36px;
  color: #4987A1;
  margin-right: 8rem;
}



.image-text-container {
  display: flex;
  align-items: center;

}

.ellipse {
  width: 100px;
  height: 100px;
  border-radius: 78px;
  background: url('~@/assets/Guy.png') center/cover;
  margin-right: 10px;
}

#ellipse813 {
  background: #000000;
  opacity: 0.3;
}

.text-info {
  display: flex;
  flex-direction: column;
}

.name,
.email,
.time,
.view-details,
.dental-implant {
  font-family: 'Inter';
  font-style: normal;
}

.name {
  font-weight: 700;
  font-size: 15px;
  line-height: 24px;
  color: #000000;
}

.email {
  font-weight: 400;
  font-size: 10px;
  line-height: 14px;
  color: #B7B7B7;
}

.time {
  font-weight: 400;
  font-size: 15px;
  line-height: 24px;
  color: #B7B7B7;
}

.dental-implant {
  font-weight: 700;
  font-size: 20px;
  line-height: 24px;
  color: #B7B7B7;
}
</style>
