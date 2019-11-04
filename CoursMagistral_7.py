#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ALGO1-:-Introduction-à-l'algorithmique" data-toc-modified-id="ALGO1-:-Introduction-à-l'algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><a href="https://perso.crans.org/besson/teach/info1_algo1_2019/" target="_blank">ALGO1 : Introduction à l'algorithmique</a></a></div><div class="lev1 toc-item"><a href="#Cours-Magistral-7" data-toc-modified-id="Cours-Magistral-7-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Cours Magistral 7</a></div><div class="lev2 toc-item"><a href="#Optimisation-de-chaînes-de-multiplications-de-matrices" data-toc-modified-id="Optimisation-de-chaînes-de-multiplications-de-matrices-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Optimisation de chaînes de multiplications de matrices</a></div><div class="lev3 toc-item"><a href="#Par-exemple-:-avec-$A_1$-de-taille-$(10,100)$,-$A_2$-de-taille-$(100,5)$-et-$A_3$-de-taille-$(5,50)$." data-toc-modified-id="Par-exemple-:-avec-$A_1$-de-taille-$(10,100)$,-$A_2$-de-taille-$(100,5)$-et-$A_3$-de-taille-$(5,50)$.-211"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Par exemple : avec <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-407-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>1</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3564" style="width: 1.368em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.13em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.216em, 1001.13em, 2.316em, -1000em); top: -2.024em; left: 0em;"><span class="mrow" id="MathJax-Span-3565"><span class="msubsup" id="MathJax-Span-3566"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.194em, 1000.69em, 4.143em, -1000em); top: -4.002em; left: 0em;"><span class="mi" id="MathJax-Span-3567" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span><span style="position: absolute; top: -3.852em; left: 0.717em;"><span class="mn" id="MathJax-Span-3568" style="font-size: 70.7%; font-family: STIXMathJax_Main;">1</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.024em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.233em; border-left: 0px solid; width: 0px; height: 1.075em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-407">A_1</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-408-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>10</mn><mo>,</mo><mn>100</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3569" style="width: 4.287em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.625em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.725em, 1003.58em, 2.861em, -1000em); top: -2.542em; left: 0em;"><span class="mrow" id="MathJax-Span-3570"><span class="mo" id="MathJax-Span-3571" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-3572" style="font-family: STIXMathJax_Main;">10</span><span class="mo" id="MathJax-Span-3573" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-3574" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">100</span><span class="mo" id="MathJax-Span-3575" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.542em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.264em; border-left: 0px solid; width: 0px; height: 1.118em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>10</mn><mo>,</mo><mn>100</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-408">(10,100)</script>, <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-409-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>2</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3576" style="width: 1.368em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.13em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.216em, 1001.13em, 2.316em, -1000em); top: -2.024em; left: 0em;"><span class="mrow" id="MathJax-Span-3577"><span class="msubsup" id="MathJax-Span-3578"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.194em, 1000.69em, 4.143em, -1000em); top: -4.002em; left: 0em;"><span class="mi" id="MathJax-Span-3579" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span><span style="position: absolute; top: -3.852em; left: 0.717em;"><span class="mn" id="MathJax-Span-3580" style="font-size: 70.7%; font-family: STIXMathJax_Main;">2</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.024em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.233em; border-left: 0px solid; width: 0px; height: 1.075em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-409">A_2</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-410-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>100</mn><mo>,</mo><mn>5</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3581" style="width: 3.675em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.107em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.713em, 1003.06em, 2.861em, -1000em); top: -2.542em; left: 0em;"><span class="mrow" id="MathJax-Span-3582"><span class="mo" id="MathJax-Span-3583" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-3584" style="font-family: STIXMathJax_Main;">100</span><span class="mo" id="MathJax-Span-3585" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-3586" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">5</span><span class="mo" id="MathJax-Span-3587" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.542em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.264em; border-left: 0px solid; width: 0px; height: 1.132em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>100</mn><mo>,</mo><mn>5</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-410">(100,5)</script> et <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-411-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>3</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3588" style="width: 1.368em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.13em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.216em, 1001.13em, 2.326em, -1000em); top: -2.024em; left: 0em;"><span class="mrow" id="MathJax-Span-3589"><span class="msubsup" id="MathJax-Span-3590"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.194em, 1000.69em, 4.143em, -1000em); top: -4.002em; left: 0em;"><span class="mi" id="MathJax-Span-3591" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span><span style="position: absolute; top: -3.852em; left: 0.717em;"><span class="mn" id="MathJax-Span-3592" style="font-size: 70.7%; font-family: STIXMathJax_Main;">3</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.024em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.244em; border-left: 0px solid; width: 0px; height: 1.087em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>3</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-411">A_3</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-412-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>5</mn><mo>,</mo><mn>50</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3593" style="width: 3.063em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.589em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.713em, 1002.54em, 2.861em, -1000em); top: -2.542em; left: 0em;"><span class="mrow" id="MathJax-Span-3594"><span class="mo" id="MathJax-Span-3595" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-3596" style="font-family: STIXMathJax_Main;">5</span><span class="mo" id="MathJax-Span-3597" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-3598" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">50</span><span class="mo" id="MathJax-Span-3599" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.542em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.264em; border-left: 0px solid; width: 0px; height: 1.132em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>5</mn><mo>,</mo><mn>50</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-412">(5,50)</script>.</a></div><div class="lev3 toc-item"><a href="#Par-exemple-:-avec-$A_1$-de-taille-$(10,100)$,-$A_2$-de-taille-$(100,5)$-et-$A_3$-de-taille-$(5,50)$-et-$A_4$-de-taille-$(50,-200)." data-toc-modified-id="Par-exemple-:-avec-$A_1$-de-taille-$(10,100)$,-$A_2$-de-taille-$(100,5)$-et-$A_3$-de-taille-$(5,50)$-et-$A_4$-de-taille-$(50,-200).-212"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Par exemple : avec <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-413-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>1</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3600" style="width: 1.368em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.13em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.216em, 1001.13em, 2.316em, -1000em); top: -2.024em; left: 0em;"><span class="mrow" id="MathJax-Span-3601"><span class="msubsup" id="MathJax-Span-3602"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.194em, 1000.69em, 4.143em, -1000em); top: -4.002em; left: 0em;"><span class="mi" id="MathJax-Span-3603" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span><span style="position: absolute; top: -3.852em; left: 0.717em;"><span class="mn" id="MathJax-Span-3604" style="font-size: 70.7%; font-family: STIXMathJax_Main;">1</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.024em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.233em; border-left: 0px solid; width: 0px; height: 1.075em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-413">A_1</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-414-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>10</mn><mo>,</mo><mn>100</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3605" style="width: 4.287em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.625em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.725em, 1003.58em, 2.861em, -1000em); top: -2.542em; left: 0em;"><span class="mrow" id="MathJax-Span-3606"><span class="mo" id="MathJax-Span-3607" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-3608" style="font-family: STIXMathJax_Main;">10</span><span class="mo" id="MathJax-Span-3609" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-3610" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">100</span><span class="mo" id="MathJax-Span-3611" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.542em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.264em; border-left: 0px solid; width: 0px; height: 1.118em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>10</mn><mo>,</mo><mn>100</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-414">(10,100)</script>, <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-415-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>2</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3612" style="width: 1.368em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.13em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.216em, 1001.13em, 2.316em, -1000em); top: -2.024em; left: 0em;"><span class="mrow" id="MathJax-Span-3613"><span class="msubsup" id="MathJax-Span-3614"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.194em, 1000.69em, 4.143em, -1000em); top: -4.002em; left: 0em;"><span class="mi" id="MathJax-Span-3615" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span><span style="position: absolute; top: -3.852em; left: 0.717em;"><span class="mn" id="MathJax-Span-3616" style="font-size: 70.7%; font-family: STIXMathJax_Main;">2</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.024em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.233em; border-left: 0px solid; width: 0px; height: 1.075em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-415">A_2</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-416-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>100</mn><mo>,</mo><mn>5</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3617" style="width: 3.675em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.107em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.713em, 1003.06em, 2.861em, -1000em); top: -2.542em; left: 0em;"><span class="mrow" id="MathJax-Span-3618"><span class="mo" id="MathJax-Span-3619" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-3620" style="font-family: STIXMathJax_Main;">100</span><span class="mo" id="MathJax-Span-3621" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-3622" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">5</span><span class="mo" id="MathJax-Span-3623" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.542em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.264em; border-left: 0px solid; width: 0px; height: 1.132em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>100</mn><mo>,</mo><mn>5</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-416">(100,5)</script> et <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-417-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>3</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3624" style="width: 1.368em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.13em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.216em, 1001.13em, 2.326em, -1000em); top: -2.024em; left: 0em;"><span class="mrow" id="MathJax-Span-3625"><span class="msubsup" id="MathJax-Span-3626"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.194em, 1000.69em, 4.143em, -1000em); top: -4.002em; left: 0em;"><span class="mi" id="MathJax-Span-3627" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span><span style="position: absolute; top: -3.852em; left: 0.717em;"><span class="mn" id="MathJax-Span-3628" style="font-size: 70.7%; font-family: STIXMathJax_Main;">3</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.024em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.244em; border-left: 0px solid; width: 0px; height: 1.087em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>3</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-417">A_3</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-418-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>5</mn><mo>,</mo><mn>50</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3629" style="width: 3.063em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.589em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.713em, 1002.54em, 2.861em, -1000em); top: -2.542em; left: 0em;"><span class="mrow" id="MathJax-Span-3630"><span class="mo" id="MathJax-Span-3631" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-3632" style="font-family: STIXMathJax_Main;">5</span><span class="mo" id="MathJax-Span-3633" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-3634" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">50</span><span class="mo" id="MathJax-Span-3635" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.542em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.264em; border-left: 0px solid; width: 0px; height: 1.132em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>5</mn><mo>,</mo><mn>50</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-418">(5,50)</script> et <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-419-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>4</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3636" style="width: 1.368em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.13em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.216em, 1001.13em, 2.316em, -1000em); top: -2.024em; left: 0em;"><span class="mrow" id="MathJax-Span-3637"><span class="msubsup" id="MathJax-Span-3638"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.194em, 1000.69em, 4.143em, -1000em); top: -4.002em; left: 0em;"><span class="mi" id="MathJax-Span-3639" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span><span style="position: absolute; top: -3.852em; left: 0.717em;"><span class="mn" id="MathJax-Span-3640" style="font-size: 70.7%; font-family: STIXMathJax_Main;">4</span><span style="display: inline-block; width: 0px; height: 4.002em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.024em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.233em; border-left: 0px solid; width: 0px; height: 1.075em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>4</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-419">A_4</script> de taille $(50, 200).</a></div><div class="lev2 toc-item"><a href="#Plus-longue-sous-séquence-commune" data-toc-modified-id="Plus-longue-sous-séquence-commune-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Plus longue sous séquence commune</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Bellman-Ford" data-toc-modified-id="Algorithme-de-Bellman-Ford-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Algorithme de Bellman-Ford</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Floyd-Warshall" data-toc-modified-id="Algorithme-de-Floyd-Warshall-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Algorithme de Floyd-Warshall</a></div><div class="lev2 toc-item"><a href="#Résolution-du-problème-du-sac-à-dos-par-programmation-dynamique" data-toc-modified-id="Résolution-du-problème-du-sac-à-dos-par-programmation-dynamique-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Résolution du problème du sac à dos par programmation dynamique</a></div><div class="lev2 toc-item"><a href="#Mémoïzation-générique" data-toc-modified-id="Mémoïzation-générique-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Mémoïzation générique</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-27"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Conclusion</a></div>

# # [ALGO1 : Introduction à l'algorithmique](https://perso.crans.org/besson/teach/info1_algo1_2019/)
# 
# - [Page du cours](https://perso.crans.org/besson/teach/info1_algo1_2019/) : https://perso.crans.org/besson/teach/info1_algo1_2019/
# - Magistère d'Informatique de Rennes - ENS Rennes - Année 2019/2020
# - Intervenants :
#   + Cours : [Lilian Besson](https://perso.crans.org/besson/)
#   + Travaux dirigés : [Raphaël Truffet](http://perso.eleves.ens-rennes.fr/people/Raphael.Truffet/)
# - Références :
#   + [Open Data Structures](http://opendatastructures.org/ods-python.pdf)

# # Cours Magistral 7
# 
# - Ce cours traite des algorithmes par programmation dynamique.

# ## Optimisation de chaînes de multiplications de matrices

# In[1]:


# https://github.com/jilljenn/tryalgo/blob/master/tryalgo/matrix_chain_mult.py
def matrix_mult_opt_order(M):
    """Matrix chain multiplication optimal order

    :param M: list of matrices
    :returns: matrices opt, arg, such that opt[i][j] is the optimal number of
              operations to compute M[i] * ... * M[j] when done in the order
              (M[i] * ... * M[k]) * (M[k + 1] * ... * M[j]) for k = arg[i][j]
    :complexity: :math:`O(n^2)`
    """
    n = len(M)
    r = [len(Mi) for Mi in M]
    c = [len(Mi[0]) for Mi in M]
    opt = [[0 for j in range(n)] for i in range(n)]
    arg = [[None for j in range(n)] for i in range(n)]
    for j_i in range(1, n):   # loop on i, j of increasing j - i = j_i
        for i in range(n - j_i):
            j = i + j_i
            opt[i][j] = float('inf')
            for k in range(i, j):
                alt = opt[i][k] + opt[k + 1][j] + r[i] * c[k] * c[j]
                if opt[i][j] > alt:
                    opt[i][j] = alt
                    arg[i][j] = k
    return opt, arg


# In[4]:


def matrix_chain_mult(M):
    """Matrix chain multiplication

    :param M: list of matrices
    :returns: M[0] * ... * M[-1], computed in time optimal order
    :complexity: whatever is needed by the multiplications
    """
    opt, arg = matrix_mult_opt_order(M)
    return apply_order(M, arg, 0, len(M)-1)


# In[5]:


def apply_order(M, arg, i, j):
    # --- multiply matrices from M[i] to M[j] included
    if i == j:
        return M[i]
    else:
        k = arg[i][j]        # --- follow placement of parentheses
        A = apply_order(M, arg, i, k)
        B = apply_order(M, arg, k + 1, j)
        row_A = range(len(A))
        row_B = range(len(B))
        col_B = range(len(B[0]))
        return [[sum(A[a][b] * B[b][c] for b in row_B)
                 for c in col_B] for a in row_A]


# Et juste pour avoir une comparaison honnête avec les multiplications de Numpy, on écrit les mêmes fonctions mais utilisant `A @ B` (`numpy.dot`) pour multiplier les matrices :

# In[40]:


def apply_order_numpy(M, arg, i, j):
    # --- multiply matrices from M[i] to M[j] included
    if i == j:
        return M[i]
    else:
        k = arg[i][j]        # --- follow placement of parentheses
        A = apply_order_numpy(M, arg, i, k)
        B = apply_order_numpy(M, arg, k + 1, j)
        return A @ B


# In[41]:


def matrix_chain_mult_numpy(M):
    """Matrix chain multiplication

    :param M: list of matrices
    :returns: M[0] * ... * M[-1], computed in time optimal order
    :complexity: whatever is needed by the multiplications
    """
    opt, arg = matrix_mult_opt_order(M)
    return apply_order_numpy(M, arg, 0, len(M)-1)


# ### Par exemple : avec $A_1$ de taille $(10,100)$, $A_2$ de taille $(100,5)$ et $A_3$ de taille $(5,50)$.

# In[42]:


import numpy as np


# In[43]:


A1 = np.random.randint(-1000, 1000, size=(10, 100))
A2 = np.random.randint(-1000, 1000, size=(100, 5))
A3 = np.random.randint(-1000, 1000, size=(5, 50))


# In[44]:


np.shape(A1)
np.shape(A2)
np.shape(A3)


# In[45]:


prod0 = A1 @ A2 @ A3  # let Python decide the order !

prod1 = (A1 @ A2) @ A3
assert np.alltrue(prod0 == prod1)

prod2 = A1 @ (A2 @ A3)
assert np.alltrue(prod0 == prod2)

assert np.alltrue(prod1 == prod2)


# In[27]:


np.shape(prod1)
np.shape(prod2)


# In[28]:


get_ipython().run_line_magic('timeit', 'A1 @ A2 @ A3')
get_ipython().run_line_magic('timeit', '(A1 @ A2) @ A3')
get_ipython().run_line_magic('timeit', 'A1 @ (A2 @ A3)')


# Python utilise l'associativité à gauche, par défaut, comme le montre les calculs ci dessus : `A1 @ A2 @ A3` est calculé comme `(A1 @ A2) @ A3`.
# On peut le vérifier avec un autre exemple :

# In[32]:


10 - 3 - 2
(10 - 3) - 2  # x - y - z = (x - y) - z oui
10 - (3 - 2)  # x - y - z != x - (y - z) non


# In[46]:


M = [A1, A2, A3]
get_ipython().run_line_magic('timeit', 'matrix_chain_mult(M)')
get_ipython().run_line_magic('timeit', 'matrix_chain_mult_numpy(M)')


# In[29]:


print("Finding the optimal order to multiply chain of matrices of dimensions")
print([np.shape(Mi) for Mi in M])
opt, arg = matrix_mult_opt_order(M)
print("opt =", opt)
print("arg =", arg)


# Ce vecteur `arg` nous dit qu'il faut d'abord multiplier `M[0]` avec `M[1]` (soit `A1 @ A2`), puis multiplier le résultat avec `M[2]` (soit `(A1 @ A2) @ A3` comme trouvé ci dessus).

# ### Par exemple : avec $A_1$ de taille $(10,100)$, $A_2$ de taille $(100,5)$ et $A_3$ de taille $(5,50)$ et $A_4$ de taille $(50, 200).

# In[47]:


A1 = np.random.randint(-1000, 1000, size=(10, 100))
A2 = np.random.randint(-1000, 1000, size=(100, 5))
A3 = np.random.randint(-1000, 1000, size=(5, 50))
A4 = np.random.randint(-1000, 1000, size=(50, 200))


# In[48]:


prod0 = A1 @ A2 @ A3 @ A4  # let Python decide the order !

prod1 = ((A1 @ A2) @ A3) @ A4
assert np.alltrue(prod0 == prod1)

prod2 = (A1 @ (A2 @ A3)) @ A4
assert np.alltrue(prod0 == prod2)

prod3 = (A1 @ A2) @ (A3 @ A4)
assert np.alltrue(prod0 == prod3)

prod4 = A1 @ ((A2 @ A3) @ A4)
assert np.alltrue(prod0 == prod4)

prod5 = A1 @ (A2 @ (A3 @ A4))
assert np.alltrue(prod0 == prod5)


# In[49]:


np.shape(prod1)
np.shape(prod2)
np.shape(prod3)
np.shape(prod4)
np.shape(prod5)


# In[50]:


get_ipython().run_line_magic('timeit', 'A1 @ A2 @ A3 @ A4')

get_ipython().run_line_magic('timeit', '((A1 @ A2) @ A3) @ A4')
get_ipython().run_line_magic('timeit', '(A1 @ (A2 @ A3)) @ A4')
get_ipython().run_line_magic('timeit', '(A1 @ A2) @ (A3 @ A4)')
get_ipython().run_line_magic('timeit', 'A1 @ ((A2 @ A3) @ A4)')
get_ipython().run_line_magic('timeit', 'A1 @ (A2 @ (A3 @ A4))')


# In[54]:


M = [A1, A2, A3, A4]
get_ipython().run_line_magic('timeit', 'matrix_chain_mult(M)')
get_ipython().run_line_magic('timeit', 'matrix_chain_mult_numpy(M)')


# In[55]:


print("Finding the optimal order to multiply chain of matrices of dimensions")
print([np.shape(Mi) for Mi in M])
opt, arg = matrix_mult_opt_order(M)
print("opt =", opt)
print("arg =", arg)


# ---
# ## Plus longue sous séquence commune

# In[13]:


def longest_common_subsequence(x, y):
    """Longest common subsequence

    Dynamic programming

    :param x:
    :param y: x, y are lists or strings
    :returns: longest common subsequence in form of a string
    :complexity: `O(|x|*|y|)`
    """
    n = len(x)
    m = len(y)
    #                      -- compute optimal length
    A = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                A[i + 1][j + 1] = A[i][j] + 1
            else:
                A[i + 1][j + 1] = max(A[i][j + 1],  A[i + 1][j])
    #                      -- extract solution
    sol = []
    i, j = n, m
    while A[i][j] > 0:
        if A[i][j] == A[i - 1][j]:
            i -= 1
        elif A[i][j] == A[i][j - 1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            sol.append(x[i])
    return ''.join(sol[::-1])    # inverse solution


# Exemples :

# In[14]:


longest_common_subsequence("BABAR", "ACAB")


# In[15]:


longest_common_subsequence("J'aime bien les oiseaux !", "Les oiseaux sont des animaux à protéger.")


# In[16]:


longest_common_subsequence("Je suis amoureux de la vie", "Tu n'es pas amoureux d'elle ?")


# ---
# ## Algorithme de Bellman-Ford

# In[25]:


def bellman_ford(graph, weight, source=0):
    """ Single source shortest paths by Bellman-Ford

    :param graph: directed graph in listlist or listdict format
    :param weight: can be negative.
                   in matrix format or same listdict graph
    :returns: distance table, precedence table, bool
    :explanation: bool is True if a negative circuit is
                  reachable from the source, circuits
                  can have length 2.
    :complexity: `O(|V|*|E|)`
    """
    n = len(graph)
    dist = [float('inf')] * n
    prec = [None] * n
    dist[source] = 0
    for nb_iterations in range(n):
        changed = False
        for node in range(n):
            for neighbor in graph[node]:
                alt = dist[node] + weight[node][neighbor]
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prec[neighbor] = node
                    changed = True
        if not changed:                   # fixed point
            return dist, prec, False
    return dist, prec, True


# Un exemple de graphe, comme celui utilisé [dans la page Wikipédia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm#Example) :

# In[26]:


oo = float('+inf')

weight = [
    [0, oo, -2, oo],
    [4, 0, 3, oo],
    [oo, oo, 0, 2],
    [oo, -1, oo, 0],
]


# In[27]:


n = len(weight)
graph = [
    [ v for v in range(n) if weight[u][v] < oo ]
    for u in range(n)
]


# In[28]:


bellman_ford(graph, weight)


# ---
# ## Algorithme de Floyd-Warshall

# In[17]:


from copy import deepcopy


# In[18]:


def floyd_warshall(weight):
    """All pairs shortest paths by Floyd-Warshall

    :param weight: edge weight matrix
    :returns: weight, and True if there are negative cycles
    :complexity: :math:`O(|V|^3)`
    """
    weight = deepcopy(weight)
    V = range(len(weight))
    for k in V:  # considering paths using 0..k
        # to go from u to v
        for u in V:
            for v in V:
                weight[u][v] = min(weight[u][v],
                                   weight[u][k] + weight[k][v])
    for v in V:
        if weight[v][v] < 0:      # negative cycle found
            return weight, True
    return weight, False


# Un exemple de graphe, comme celui utilisé [dans la page Wikipédia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm#Example) :

# In[21]:


oo = float('+inf')

weight = [
    [0, oo, -2, oo],
    [4, 0, 3, oo],
    [oo, oo, 0, 2],
    [oo, -1, oo, 0],
]


# In[22]:


floyd_warshall(weight)


# <img width="75%" src="figures/CM7_Floyd-Warshall.png">

# ---
# ## Résolution du problème du sac à dos par programmation dynamique

# In[29]:


def knapsack(p, v, cmax):
    """Knapsack problem: select maximum value set of items if total size not
    more than capacity

    :param p: table with size of items
    :param v: table with value of items
    :param cmax: capacity of bag
    :requires: number of items non-zero
    :returns: value optimal solution, list of item indexes in solution
    :complexity: O(n * cmax), for n = number of items
    """
    n = len(p)
    opt = [[0] * (cmax + 1) for _ in range(n + 1)]
    sel = [[False] * (cmax + 1) for _ in range(n + 1)]
    #                               --- basic case
    for cap in range(p[0], cmax + 1):
        opt[0][cap] = v[0]
        sel[0][cap] = True
    #                               --- induction case
    for i in range(1, n):
        for cap in range(cmax + 1):
            if cap >= p[i] and opt[i-1][cap - p[i]] + v[i] > opt[i-1][cap]:
                opt[i][cap] = opt[i-1][cap - p[i]] + v[i]
                sel[i][cap] = True
            else:
                opt[i][cap] = opt[i-1][cap]
                sel[i][cap] = False
    #                               --- reading solution
    cap = cmax
    solution = []
    for i in range(n-1, -1, -1):
        if sel[i][cap]:
            solution.append(i)
            cap -= p[i]
    return (opt[n - 1][cmax], solution)


# On peut considérer l'exemple de la page Wikipédia :
# 
# For example, there are 10 different items and the weight limit is 67.
# And with : $$\begin{align}
# &w[  1]= 23 ,w[  2]= 26,w[  3]= 20,w[  4]= 18,w[  5]= 32,w[  6]= 27,w[  7]= 29,w[  8]= 26,w[  9]= 30,w[ 10]= 27 \\
# &v[  1]=505 ,v[  2]=352,v[  3]=458,v[  4]=220,v[  5]=354,v[  6]=414,v[  7]=498,v[  8]=545,v[  9]=473,v[ 10]=543 \\
# \end{align}$$

# In[30]:


p = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]  # param p, table with size of items
v = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]  # param v, table with value of items
cmax = 67  # param cmax, capacity of bag


# In[31]:


knapsack(p, v, cmax)


# $$\begin{align}
# &m(10, 67) = 1270\\
# &m(9, 67) = 1270, m(9, 40) = 678\\
# &m(8, 67) = 1270, m(8, 40) = 678, m(8, 37) = 545\\
# &m(7, 67) = 1183, m(7, 41) = 725, m(7, 40) = 678, m(7, 37) = 505\\
# &m(6, 67) = 1183, m(6, 41) = 725, m(6, 40) = 678, m(6, 38) = 678, m(6, 37) = 505\\
# &m(5, 67) = 1183, m(5, 41) = 725, m(5, 40) = 678, m(5, 38) = 678, m(5, 37) = 505\\
# &m(4, 67) = 1183, m(4, 41) = 725, m(4, 40) = 678, m(4, 38) = 678, m(4, 37) = 505, m(4, 35) = 505\\
# &m(3, 67) = 963, m(3, 49) = 963, m(3, 41) = 505, m(3, 40) = 505, m(3, 38) = 505, m(3, 37) = 505, m(3, 35) = 505, m(3, 23) = 505, m(3, 22) = 458, m(3, 20) = 458\\
# &m(2, 67) = 857, m(2, 49) = 857, m(2, 47) = 505, m(2, 41) = 505, m(2, 40) = 505, m(2, 38) = 505, m(2, 37) = 505, m(2, 35) = 505, m(2, 29) = 505, m(2, 23) = 505\\
# &m(1, 67) = 505, m(1, 49) = 505, m(1, 47) = 505, m(1, 41) = 505, m(1, 40) = 505, m(1, 38) = 505, m(1, 37) = 505, m(1, 35) = 505, m(1, 29) = 505, m(1, 23) = 505\\
# \end{align}$$

# ---
# ## Mémoïzation générique

# In[1]:


from time import sleep


# In[2]:


def f1(n):
    sleep(3)
    return n + 3


# In[3]:


print("3 secondes...")
print(f1(10))  # 13, 3 secondes après


# In[4]:


def f2(n):
    sleep(4)
    return n * n


# In[5]:


print("4 secondes...")
print(f2(10))  # 100, 4 secondes après


# Mémoïsation générique, non typée

# In[6]:


def memo(f):
    memoire = {}  # dictionnaire vide, {} ou dict()
    def memo_f(n):
        if n not in memoire:
             memoire[n] = f(n)
        return memoire[n]
    return memo_f


# In[7]:


memo_f1 = memo(f1)

print("3 secondes...")
print(memo_f1(10))  # 13, 3 secondes après
print("0 secondes !")
print(memo_f1(10))  # instantanné !


# In[8]:


# différent de ces deux lignes !

print("3 secondes...")
print(memo(f1)(10))
print("3 secondes...")
print(memo(f1)(10))  # 3 secondes aussi !


# In[9]:


memo_f2 = memo(f2)

print("4 secondes...")
print(memo_f2(10))  # 100, 4 secondes après
print("0 secondes !")
print(memo_f2(10))  # instantanné !


# In[10]:


# bonus : on peut utiliser la syntaxe d'un décorateur en Python :

def fibo(n):
    if n <= 1: return 1
    else: return fibo(n-1) + fibo(n-2)

print("Test de fibo() non mémoisée :")
for n in range(10):
    print("F_{} = {}".format(n, fibo(n)))


# In[11]:


# version plus rapide !
@memo
def fibo(n):
    if n <= 1: return 1
    else: return fibo(n-1) + fibo(n-2)

print("Test de fibo() mémoisée (plus rapide) :")
for n in range(10):
    print("F_{} = {}".format(n, fibo(n)))


# In[12]:


@memo
def factorielle(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return n * factorielle(n-1)

print("Test de factorielle() mémoisée :")
for n in range(10):
    print("{}! = {}".format(n, factorielle(n)))


# ## Conclusion
# 
# C'est bon pour aujourd'hui !
