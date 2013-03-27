電子元件分類
############

:slug: electronic-component
:date: 2013-03-26 15:25
:tags: electronic, arduino, raspberrypi
:category: Electronic
:author: MagicSword
:lang: zh-tw
:summary: 整理一下電子元件的種類，引用Wiki，之後再加入自已的整理，
          和一些使用心得。


電子元件分類
============

依性質可以被動或主動的（passive or active）：
  * 被動：沒有方向性、或是增益
  * 主動：有方向性、主動發出增益


開關
====

* 能夠控制電路的開路或閉路的電子元件
* 開關（Switch）- 手動操作的開關
* Keypad - 一群按鈕開關的集合（例如只能輸入數字的小鍵盤）
* 繼電器（Relay） - 電流操作的開關。它是一種電磁元件，有別於固態繼電器（Solid State Relay）
	* 電磁開關（Contactor）

* 自動調溫器（Thermostat） - 溫度致動的開關
* 斷路器（Circuit Breaker） - 過電流致動的開關
* 限位開關（Limit switch） - 機械式的啟動開關
* 水銀開關（Mercury switch）
* 離心開關（Centrifugal switch）


電阻
====

電阻類的電子元件
	1. 參見下方「感測器」段落中的電阻，用於環境檢測
	2. 參見下方「保護裝置」段落中的電阻，用於限制電流或電壓

* 電阻器（Resistor）- 固定的電阻值
* 電阻網路（Resistor network）
* Trimmer - 小型可變電阻器
* 可變電阻 - 可變的電阻值
* 加熱器 - 電熱元件（en:heating element）
* 電熱線（en:Resistance wire） - 高電阻材質的線，近似於加熱元件
* 熱敏電阻（Thermistor）- 溫度改變電阻值
* 壓敏電阻（Varistor）- 變壓電阻



保護裝置
========

在過高的電壓或電流之中保護電路的被動元件
	雖然這些元件，在技術上屬於電線、電阻或真空管類，但根據它們的用途列於下方。
	主動元件，在半導體類中屬於執行保護功能，如下。

* 保險絲（Fuse）- 過電流保護，只能使用一次。
* 自恢復保險絲 (PolySwitch, self-resetting fuse)- 過電流保護，可重設後重複使用
* 金屬氧化物壓敏電阻、突波吸收器 (MOV) - 過電壓保護，這些是被動元件，不像是TVS
* 突波電流限制器（Inrush current limiter） - 避免突波電流（Inrush current）造成損壞
* 氣體放電管（Gas Discharge Tube）
* 斷路器（Circuit Breaker）- 過電流致動的開關
* 積熱電驛（Thermal Realy）- 過電流致動的開關
* 白熾燈
* 接地漏電保護插座（GFCI）或 RCD


電容
====

在電場存儲的電荷的元件。 電容器在電路中用於過濾。 電容器通常會改變所通過的交流電壓，而不會改變恆定的直流電壓。

* 電容器（Capacitor） - 固定的電容量
* 電容電路（Capacitor network）
* 可變電容器（Variable capacitor）- 能夠改變的電容量
* 變容二極體（Varicap diode）- 能夠改變的電容量的二極體


電磁感應裝置
============

使用磁的電子元件

* 電感元件（Inductor）
* 可變電感器（Variable inductor）
* 變壓器（Transformer）
* 電動機（Motor）/ 發電機（Generator）
* 螺線管（Solenoid）
* 揚聲器（Speaker）/ 麥克風（Microphone）


網路（network）
===============

使用多個或多種類型的被動元件組成的複合電路元件，英文稱為network，但中文裡通常不使用網路這種稱呼。
排阻或電阻排

* 憶阻器（Memristor）

壓電裝置、晶體諧振器
====================

使用壓電效應的被動元件

* 石英晶體諧振器（crystal oscillator）
* 壓電電動機（Ultrasonic motor）- 使用壓電效應的電動機


電源
====

電力來源

* 電池（Battery）
* 燃料電池（Fuel cell）- 使用燃料進行化學反應產生電力的裝置
* 電源供應（Power supply）
* 太陽能電池（Photo voltaic device）
* 發電機（Electrical generator）


感測器
======

* 感測器（Sensor）
	* 揚聲器（Loudspeaker）
	* 加速度感測器（Accelerometer）

* Thermal
	* 熱電偶（Thermocouple）, 熱電堆（thermopile）
	* 熱敏電阻（Thermistor）
	* 電阻溫度計（Resistance Temperature Detector、RTD）
	* 輻射熱測量計（Bolometer）

* 磁場（Magnetic field）

* 濕度（Humidity）
	* 濕度計（Hygrometer）
	* 光敏電阻（Photo resistor）

固態電子元件, 半導體
====================

二極體
------

這類的電子元件能夠控制電流方向是單向的。

* 二極體（Diode）, 整流器（Rectifier）, 橋式整流器（Bridge Rectifier）
* 蕭特基二極體（Schottky Diode）
* 齊納二極體（Zener Diode）
* 發光二極體（Light Emitting Diode、LED）
* 雷射二極體（LASER Diode）
* 光電二極體（Photodiode）
* 太陽能電池（Solar cell）
* 雪崩光電二極體（Avalanche Photodiode）
* 定電流二極體（Constant Current Diode, Current Regulative Diode (CRD), 或 Current Limiting Diode）: 外觀如同二極體，也有單向導通特性，但內部構造實際上是 FET 所接成。


電晶體
------

* 雙極性電晶體（Bipolar Junction Transistor、BJT）- NPN 或 PNP
	* 異質結雙極型電晶體
	* 達靈頓電晶體（Darlington transistor）- NPN 或 PNP

* 場效電晶體（Field effect transistor、FET）
	* 接面場效電晶體（Junction Field Effect Transistor、JFET） - N-通道 或 P-通道
	* 金氧半場效電晶體（Metal Oxide Semiconductor FET、MOSFET） - N-通道 或 P-通道
	* 金屬半導體場效應管 (MESFET)
	* 高電子遷移率電晶體 (HEMT)

* 晶閘管（Thyristor）
	* 單接合面電晶體 (UJT, Unijunction transistor)
	* 可程式化單接合面電晶體 (PUT, Programmable UniJunction Transistor)
	* 絕緣柵雙極電晶體（Insulated Gate Bipolar Transistor、IGBT）

積體電路
--------

* 數位積體電路（Digital circuit）
* 類比積體電路（Analog circuit）
	* 霍爾效應感測器（Hall effect sensor）

Hybrid Circuits
---------------

* 光電工程（Optoelectronics）
	* 光電耦合元件（Opto-isolator|Opto-Isolator, Opto-Coupler, Photo-Coupler)
	* LED Display - 七段顯示器（Seven-segment display）, Sixteen-segment display, Dot matrix display

顯示科技
========

現在:

* 白熾燈（Filament lamp）
* 真空熒光顯示器 （Vacuum fluorescent display、VFD） (preformed characters, 七段顯示器, starburst)
* 陰極射線管（Cathode ray tube、CRT） (dot matrix scan (eg CRT顯示器), radial scan (eg 雷達), arbitrary scan (eg 示波器)) (單色 & 彩色)
* 霓虹燈（Neon lamp）- 使用氖（Neon）
* 電漿顯示器（Plasma display）

過時:

* 數碼管（Nixie Tube）
* 幻眼管（Magic eye tube）

真空管
======

* 運作在真空中的主動元件
	* 二極真空管（Diode）
	* 三極真空管（Triode）
	* 四極真空管（Tetrode）
	* 五極真空管（Pentode）
	* 六極管（Hexode）
	* 五柵變頻管（Pentagrid Converter）
	* 八極管（Octode）
	* Barretter
	* 小型抗震管（Nuvistor）
	* 小型電子管（Compactron）

微波（Microwave）
	* 速電管
	* 磁電管

光學（Optical）
	* 光電二極體（Photodiode）
	* 陰極射線管（Cathode ray tube、CRT）
	* 真空熒光顯示器（Vacuum fluorescent display、VFD）
	* 光電倍增管（Photomultiplier）
	* X射線管（X-ray tube）

組件、模組
==========

多個電子元件被組裝在一起，作為一個元件

* 振蕩器

* 顯示設備
	* 液晶顯示器 (LCD)

* 電子濾波器 （Filter）
	* 天線 （Antennas）
	* 偶極天線（Dipole antenna）
	* 雙錐形天線（Biconical antenna）
	* 八木天線（Yagi antenna）
	* 相控陣天線（Phased array）
	* 磁偶極天線（Magnetic dipole）
	* 拋物面反射器（Parabolic dish）
	* 喇叭天線（Feedhorn）

其他
====

* Prototyping aids
	* 麵包板（Breadboard）
* 機械配件
	* 散熱片（Heat sink）
	* 電風扇（Fan）
* 印刷電路板（英語：Printed circuit board、縮寫：PCB）
* 端子與連接器
* 電線


標準縮寫
========

元件名稱的縮寫廣泛被應用於工業：

* AE, ANT: 天線（antenna）
* B: 電池（battery）
* BR: 橋式整流器（bridge rectifier）
* C: 電容器（capacitor）
* CRT: 陰極射線管（cathode ray tube）
* D 或 CR: 二極體（diode）
* DSP: 數位訊號處理器（digital signal processor）
* F: 保險絲（fuse）
* FET:場效電晶體（field effect transistor）
* GDT: 氣體放電管（gas discharge tube）
* IC: 積體電路（integrated circuit）
* J: 跳線或跳接點(jumper)
* JFET: 接面場效電晶體（junction gate field-effect transistor）
* L: 電感（inductor）
* LCD: 液晶顯示器（liquid crystal display）
* LDR: 光敏電組（light dependent resistor）
* LED: 發光二極體（light emitting diode）
* LS: 揚聲器（(loud) speaker）
* M: 電動機、馬達（motor），電表（meter）
* MCB: 斷路器（miniature circuit breaker）
* Mic: 麥克風（microphone）
* MOSFET:金氧半場效電晶體（metal oxide semiconductor field effect transistor）
* Ne: 霓虹燈、氖燈（neon lamp）
* OP, OPA: 運算放大器（operational amplifier）
* PCB: 印刷電路板（printed circuit board）
* Q: 三極體（transistor）
* R: 電阻器（resistor）
* RLA: RY: 繼電器（relay）
* SCR: ;矽控整流器（silicon controlled rectifier）
* SW: 開關（switch）
* T: 變壓器（transformer）
* TFT:薄膜電晶體（thin film transistor(display)）
* TH: 熱敏電阻（thermistor）
* TP: 測試點（test point）
* Tr: 三極體（transistor）
* U: 積體電路（integrated circuit）
* V: 真空管（valve (tube)）
* VC: 可變電容器（variable capacitor）
* VFD: 真空熒光顯示器（vacuum fluorescent display）
* VLSI:超大型積體電路（very large scale integration）
* VR: 可變電阻（variable resistor）
* X: 晶體振蕩器，陶瓷諧振器（crystal, ceramic resonator）
* XMER: 變壓器（transformer）
* XTAL: 晶體振蕩器（crystal）
* Z 或 ZD: 齊納二極體（Zener diode）




Reference
==========

1. `Wikipedia 電子元件 <http://zh.wikipedia.org/wiki/%E9%9B%BB%E5%AD%90%E5%85%83%E4%BB%B6>`_



.. _thisfile:
.. vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
.. template_version=0.3_20120112