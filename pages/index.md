<div class="landing">
  <section class="landing-hero" aria-labelledby="hero-title">
    <div class="hero-copy">
      <h1 id="hero-title">Good connections<br><em>stand the test of time.</em></h1>
      <p class="hero-intro">Meet Netatalk: the fastest and most versatile file sharing suite in the world. Share and access files across generations of systems.</p>
      <div class="hero-actions">
        <a class="landing-button primary" href="#start-title">Get started <span aria-hidden="true">↗</span></a>
        <a class="landing-button secondary" href="https://netatalk.io/client/manual/en/getting_started.html">Explore the client <span aria-hidden="true">→</span></a>
      </div>
    </div>
    <div class="hero-art" aria-hidden="true">
      <svg viewBox="0 0 600 500" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="300" cy="250" r="207" stroke="#a8c8f8" stroke-opacity=".35"/>
        <circle cx="300" cy="250" r="160" stroke="#a8c8f8" stroke-opacity=".35"/>
        <circle cx="300" cy="250" r="112" stroke="#a8c8f8" stroke-opacity=".35"/>
        <path d="M45 335C160 335 169 112 301 112S443 335 555 335" stroke="#3D82FF" stroke-width="3"/>
        <path d="M45 335C160 335 169 112 301 112S443 335 555 335" stroke="#19E3D2" stroke-width="9" stroke-linecap="round" stroke-dasharray="1 90"/>
        <path d="M60 165C163 165 185 386 300 386S437 165 540 165" stroke="#8BAFFF" stroke-width="2" stroke-dasharray="4 8"/>
        <rect x="208" y="165" width="184" height="164" rx="25" fill="#0B1F3A" stroke="#7DA7F6" stroke-width="2"/>
        <rect x="230" y="187" width="140" height="100" rx="8" fill="#15345B"/>
        <path d="M254 246h26l13-25 15 39 13-25h25" stroke="#19E3D2" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M270 309h60" stroke="#7DA7F6" stroke-width="4" stroke-linecap="round"/>
        <circle cx="98" cy="267" r="31" fill="#16375E" stroke="#7DA7F6" stroke-width="2"/><path d="M85 267h26M98 254v26" stroke="#19E3D2" stroke-width="3"/>
        <circle cx="501" cy="267" r="31" fill="#16375E" stroke="#7DA7F6" stroke-width="2"/><path d="M488 267h26M501 254v26" stroke="#19E3D2" stroke-width="3"/>
        <circle cx="300" cy="43" r="5" fill="#19E3D2"/><circle cx="485" cy="132" r="5" fill="#3D82FF"/><circle cx="158" cy="399" r="5" fill="#19E3D2"/>
      </svg>
      <span class="art-label art-label-one">MACINTOSH</span><span class="art-label art-label-two">UNIX / LINUX</span>
    </div>
  </section>
  <div class="landing-strip"><span>FILE SHARING, WITHOUT BOUNDARIES</span><span>AFP <i>✳</i> OPEN SOURCE <i>✳</i> <a href="https://netatalk.org">SINCE 1990</a></span></div>
  <section class="landing-start" aria-labelledby="start-title">
    <div class="start-heading"><p class="eyebrow">01 / GET CONNECTED</p><h2 id="start-title">A little setup.<br><em>A lot of connection.</em></h2><p>Start a file server, connect to one, or make Netatalk your own. Pick the path that works for you.</p></div>
    <div class="install-card">
      <div class="install-top"><div><span class="status-dot"></span> QUICK START <span class="install-sub">/ SERVER</span></div><label for="install-platform">Platform</label><select id="install-platform"><option value="docker">Docker</option><option value="debian">Debian / Ubuntu</option><option value="fedora">Fedora</option><option value="freebsd">FreeBSD</option></select></div>
      <div class="command-row"><span aria-hidden="true">$</span><code id="install-command">docker pull netatalk/netatalk</code><button id="copy-command" type="button">Copy</button></div>
      <p id="install-hint">Pull the container image to get started. Configuration is the next step.</p>
      <a href="https://netatalk.io/containers.html" id="install-guide">Container guide <span aria-hidden="true">↗</span></a>
      <noscript><p>Choose a platform above with JavaScript enabled, or see all <a href="https://netatalk.io/download.html">download options</a>.</p></noscript>
    </div>
  </section>
  <section class="landing-paths" aria-label="Explore Netatalk">
    <a class="path-card" href="https://netatalk.io/manual/en/Configuration.html"><span class="path-number">02 / SHARE</span><span class="path-icon">↗</span><h3>Set up a server</h3><p>Share files from a UNIX-like host with your Macs and AFP clients.</p><span class="path-link">Configure Netatalk →</span></a>
    <a class="path-card" href="https://netatalk.io/client/manual/en/getting_started.html"><span class="path-number">03 / CONNECT</span><span class="path-icon">⌘</span><h3>Meet the client</h3><p>Connect to AFP file servers with the Netatalk Client.</p><span class="path-link">Get started with the client →</span></a>
    <a class="path-card" href="https://netatalk.io/install.html"><span class="path-number">04 / BUILD</span><span class="path-icon" aria-hidden="true">⚒</span><h3>Make it yours</h3><p>Build from source and explore the options for your setup.</p><span class="path-link">Build Netatalk →</span></a>
  </section>
  <section class="landing-closing"><div><h2>Different machines.<br><em>Common ground.</em></h2></div><div><p>From classic Macs to modern systems, Netatalk keeps AFP file sharing open and accessible.</p><a href="https://netatalk.io/docs/">Explore the documentation ↗</a><a href="https://netatalk.io/archive.html">Project news ↗</a></div></section>
</div>
<script>
(function () {
  var choices = {
    docker: ['docker pull netatalk/netatalk', 'Pull the container image to get started. Configuration is the next step.', '/containers.html', 'Container guide'],
    debian: ['sudo apt install netatalk', 'Install the package available for your distribution, then configure the server.', '/manual/en/Configuration.html', 'Configuration guide'],
    fedora: ['sudo dnf install netatalk', 'Install the package available for your distribution, then configure the server.', '/manual/en/Configuration.html', 'Configuration guide'],
    freebsd: ['sudo pkg install netatalk', 'Install the package available for your system, then configure the server.', '/manual/en/Configuration.html', 'Configuration guide']
  };
  var select = document.getElementById('install-platform');
  var command = document.getElementById('install-command');
  var hint = document.getElementById('install-hint');
  var guide = document.getElementById('install-guide');
  var copy = document.getElementById('copy-command');
  var ua = navigator.userAgent;
  if (/Ubuntu|Debian/i.test(ua)) select.value = 'debian';
  else if (/Fedora/i.test(ua)) select.value = 'fedora';
  else if (/FreeBSD/i.test(ua)) select.value = 'freebsd';
  function update() {
    var choice = choices[select.value];
    command.textContent = choice[0]; hint.textContent = choice[1];
    guide.href = document.querySelector('.landing').dataset.base + choice[2].slice(1);
    guide.textContent = choice[3] + ' ↗'; copy.textContent = 'Copy';
  }
  var firstLink = document.querySelector('.landing a[href]');
  var installationPath = 'manual/en/Installation.html';
  var href = firstLink.getAttribute('href');
  document.querySelector('.landing').dataset.base = href.slice(0, href.length - installationPath.length);
  select.addEventListener('change', update);
  copy.addEventListener('click', function () {
    if (!navigator.clipboard) { copy.textContent = 'Select and copy'; return; }
    navigator.clipboard.writeText(command.textContent).then(function () { copy.textContent = 'Copied!'; }, function () { copy.textContent = 'Select and copy'; });
  });
  update();
})();
</script>
