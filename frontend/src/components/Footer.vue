<template>
  <footer class="footer">
    <!-- Bottom: Copyright -->
    <div class="footer-bottom">
      <div class="footer-inner">
        <p>Copyright ©2026 longkitech.com {{ $t('footer.copyright') }} | {{ $t('footer.icp') }}</p>
        <p>{{ $t('footer.phone') }}</p>
        <p>{{ $t('footer.psb') }}</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
  background: var(--color-dark);
  color: var(--color-gray-4);
  font-size: 12px;
}
.footer-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 15px;
}

/* Bottom */
.footer-bottom {
  background: var(--color-darker);
  padding: 18px 0;
  text-align: center;
  line-height: 1.8;
}
.footer-bottom p {
  color: var(--color-gray-4);
  font-size: 11px;
}

</style>
