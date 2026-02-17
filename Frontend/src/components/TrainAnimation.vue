<template>
  <div class="animation-container">
    <div class="background-text">Начни свой путь!</div>
    <div class="rocket">
      🚀
    </div>
  </div>
</template>

<script>
export default {
  name: 'TrainAnimation'
}
</script>

<style scoped>
.animation-container {
  position: relative;
  width: 100%;
  height: 250px;
  overflow: hidden;
  background: white;
}

.background-text {
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 5rem;
  font-weight: bold;
  color: rgba(255, 0, 0, 0.3);
  white-space: nowrap;
  z-index: 1;
  text-align: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

.rocket {
  position: absolute;
  bottom: 85px;
  font-size: 7.5rem;
  animation: flyRocket 15s linear infinite;
  z-index: 3;
  transform: rotate(45deg);
}

@keyframes flyRocket {
  0% {
    left: -150px;
  }
  100% {
    left: calc(100% + 150px);
  }
}

@keyframes vibrate {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-2px); }
  75% { transform: translateX(2px); }
}

@keyframes burn {
  0% { transform: scale(1); opacity: 0.8; }
  100% { transform: scale(1.2); opacity: 1; }
}
</style>