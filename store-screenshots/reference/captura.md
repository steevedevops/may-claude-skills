# Captura dos prints

## Devices e tamanhos

| Loja | Device | PNG cru |
|---|---|---|
| App Store iPhone 6,9″ | simulador iPhone 16 Pro Max (ou o emulador Android, se o usuário já tem um rodando — o design recorta igual) | 1320 × 2868 / 1080 × 2400 |
| App Store iPad 13″ | simulador iPad Pro 13-inch | 2064 × 2752 |
| Google Play celular | emulador Android de celular | 1080 × 2400 |

Se o usuário já tem um emulador rodando, use o dele. Rode UM device de cada vez: dois
`maestro test` em paralelo falham os dois.

## Maestro (2.10+)

- `takeScreenshot` só grava dentro da pasta de saída do próprio teste. Rode com
  `--test-output-dir=<tmp>`, passe `-e SAIDA=.` ao flow e depois
  `find <tmp> -name "<nome>.png"` e mova para a pasta de originais.
- O script de captura não deve apagar `originais/` quando roda só alguns flows (só
  quando roda o conjunto inteiro), senão um re-take isolado apaga os outros prints.
- Flutter no Android junta textos irmãos num único rótulo de acessibilidade
  (`"R\nOlá!\nRafael"`, `"1\nReservas Hoje\nHoje"`, abas `"Partidas\nPartidas"`). O
  Maestro compara o texto inteiro: use regex `"(?s).*Olá!.*"` ou o rótulo exato com `\n`.
  Para descobrir o rótulo real: `adb shell uiautomator dump /sdcard/u.xml` e
  `grep content-desc`.
- Cuidado com regex amplo demais: `.*Nome do Local.*` pode casar com um banner fixo do
  rodapé e tirar o print com a lista ainda carregando. Espere por um texto que só existe
  no conteúdo carregado.
- Build debug abre devagar a frio: timeouts de abertura de 120 s.
- Telas que dependem de modo salvo (Lista × Calendário): aceite os dois no `visible`.

## Emulador Android

- Barra de status: `settings put global sysui_demo_allowed 1` + broadcasts
  `com.android.systemui.demo` (clock 0941, battery 100, network full, notifications
  false). Mesmo assim ícones de push podem aparecer → `scripts/limpar_status.py`.
- Localização: `adb emu geo fix <lng> <lat>` na cidade dos dados demo, antes de abrir
  telas que usam GPS (listas por distância ficam girando sem posição).
- App instalado com outra assinatura: `INSTALL_FAILED_UPDATE_INCOMPATIBLE` →
  `adb uninstall <pacote>` e instalar de novo (o login se perde).
- Build rápida para emulador arm64: `flutter build apk --debug --target-platform android-arm64`.

## Simulador iOS (Xcode recente)

- Pods com deployment target < 15 quebram o build: ajuste o `Pods.xcodeproj`
  (`IPHONEOS_DEPLOYMENT_TARGET = 15.0`) — volta a cada `pod install`.
- `flutter build ios --simulator` pode falhar por arquitetura; use
  `xcodebuild -workspace ios/Runner.xcworkspace -scheme Runner -configuration Debug -sdk iphonesimulator -destination "id=<UDID>" ARCHS=arm64 ONLY_ACTIVE_ARCH=YES BUILD_DIR=$PWD/build/ios build`
  e `xcrun simctl install <UDID> build/ios/Debug-iphonesimulator/Runner.app`.
- Barra de status: `xcrun simctl status_bar <UDID> override --time 9:41 --batteryState charged --batteryLevel 100 --cellularBars 4 --wifiBars 3`.
- App preso no splash: veja `xcrun simctl spawn <UDID> log show --last 3m --predicate 'process == "Runner"'`.
  Clássico em Flutter/Riverpod: provider alterado no `initState` → "Tried to modify a
  provider while the widget tree was building" → mova a chamada para
  `WidgetsBinding.instance.addPostFrameCallback`.

## Revisão

Depois de cada rodada, monte a folha de contato (`scripts/folha_contato.py <pasta>`) e
olhe TODOS os prints. Refaça só os que falharam.
