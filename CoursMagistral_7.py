#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ALGO1-:-Introduction-à-l'algorithmique" data-toc-modified-id="ALGO1-:-Introduction-à-l'algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><a href="https://perso.crans.org/besson/teach/info1_algo1_2019/" target="_blank">ALGO1 : Introduction à l'algorithmique</a></a></div><div class="lev1 toc-item"><a href="#Cours-Magistral-7" data-toc-modified-id="Cours-Magistral-7-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Cours Magistral 7</a></div><div class="lev2 toc-item"><a href="#Optimisation-de-chaînes-de-multiplications-de-matrices" data-toc-modified-id="Optimisation-de-chaînes-de-multiplications-de-matrices-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Optimisation de chaînes de multiplications de matrices</a></div><div class="lev3 toc-item"><a href="#Par-exemple-:-avec-$A_1$-de-taille-$(10,100)$,-$A_2$-de-taille-$(100,5)$-et-$A_3$-de-taille-$(5,50)$." data-toc-modified-id="Par-exemple-:-avec-$A_1$-de-taille-$(10,100)$,-$A_2$-de-taille-$(100,5)$-et-$A_3$-de-taille-$(5,50)$.-211"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Par exemple : avec <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-27-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>1</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-155" style="width: 1.343em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.149em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.392em, 1001.15em, 2.497em, -1000em); top: -2.203em; left: 0em;"><span class="mrow" id="MathJax-Span-156"><span class="msubsup" id="MathJax-Span-157"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.212em, 1000.69em, 4.167em, -1000em); top: -4.023em; left: 0em;"><span class="mi" id="MathJax-Span-158" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -3.873em; left: 0.717em;"><span class="mn" id="MathJax-Span-159" style="font-size: 70.7%; font-family: STIXMathJax_Main;">1</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.203em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.23em; border-left: 0px solid; width: 0px; height: 1.059em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-27">A_1</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-28-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>10</mn><mo>,</mo><mn>100</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-160" style="width: 4.169em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.592em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.719em, 1003.54em, 2.859em, -1000em); top: -2.538em; left: 0em;"><span class="mrow" id="MathJax-Span-161"><span class="mo" id="MathJax-Span-162" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-163" style="font-family: STIXMathJax_Main;">10</span><span class="mo" id="MathJax-Span-164" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-165" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">100</span><span class="mo" id="MathJax-Span-166" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.538em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.261em; border-left: 0px solid; width: 0px; height: 1.101em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>10</mn><mo>,</mo><mn>100</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-28">(10,100)</script>, <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-29-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>2</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-167" style="width: 1.343em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.149em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.392em, 1001.15em, 2.497em, -1000em); top: -2.203em; left: 0em;"><span class="mrow" id="MathJax-Span-168"><span class="msubsup" id="MathJax-Span-169"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.212em, 1000.69em, 4.167em, -1000em); top: -4.023em; left: 0em;"><span class="mi" id="MathJax-Span-170" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -3.873em; left: 0.717em;"><span class="mn" id="MathJax-Span-171" style="font-size: 70.7%; font-family: STIXMathJax_Main;">2</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.203em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.23em; border-left: 0px solid; width: 0px; height: 1.059em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-29">A_2</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-30-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>100</mn><mo>,</mo><mn>5</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-172" style="width: 3.642em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.113em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.707em, 1003.07em, 2.859em, -1000em); top: -2.538em; left: 0em;"><span class="mrow" id="MathJax-Span-173"><span class="mo" id="MathJax-Span-174" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-175" style="font-family: STIXMathJax_Main;">100</span><span class="mo" id="MathJax-Span-176" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-177" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">5</span><span class="mo" id="MathJax-Span-178" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.538em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.261em; border-left: 0px solid; width: 0px; height: 1.115em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>100</mn><mo>,</mo><mn>5</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-30">(100,5)</script> et <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-31-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>3</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-179" style="width: 1.343em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.149em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.392em, 1001.15em, 2.507em, -1000em); top: -2.203em; left: 0em;"><span class="mrow" id="MathJax-Span-180"><span class="msubsup" id="MathJax-Span-181"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.212em, 1000.69em, 4.167em, -1000em); top: -4.023em; left: 0em;"><span class="mi" id="MathJax-Span-182" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -3.873em; left: 0.717em;"><span class="mn" id="MathJax-Span-183" style="font-size: 70.7%; font-family: STIXMathJax_Main;">3</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.203em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.241em; border-left: 0px solid; width: 0px; height: 1.07em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>3</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-31">A_3</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-32-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>5</mn><mo>,</mo><mn>50</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-184" style="width: 3.02em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.586em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.707em, 1002.54em, 2.859em, -1000em); top: -2.538em; left: 0em;"><span class="mrow" id="MathJax-Span-185"><span class="mo" id="MathJax-Span-186" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-187" style="font-family: STIXMathJax_Main;">5</span><span class="mo" id="MathJax-Span-188" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-189" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">50</span><span class="mo" id="MathJax-Span-190" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.538em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.261em; border-left: 0px solid; width: 0px; height: 1.115em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>5</mn><mo>,</mo><mn>50</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-32">(5,50)</script>.</a></div><div class="lev3 toc-item"><a href="#Par-exemple-:-avec-$A_1$-de-taille-$(10,100)$,-$A_2$-de-taille-$(100,5)$-et-$A_3$-de-taille-$(5,50)$-et-$A_4$-de-taille-$(50,-200)." data-toc-modified-id="Par-exemple-:-avec-$A_1$-de-taille-$(10,100)$,-$A_2$-de-taille-$(100,5)$-et-$A_3$-de-taille-$(5,50)$-et-$A_4$-de-taille-$(50,-200).-212"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Par exemple : avec <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-33-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>1</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-191" style="width: 1.343em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.149em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.392em, 1001.15em, 2.497em, -1000em); top: -2.203em; left: 0em;"><span class="mrow" id="MathJax-Span-192"><span class="msubsup" id="MathJax-Span-193"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.212em, 1000.69em, 4.167em, -1000em); top: -4.023em; left: 0em;"><span class="mi" id="MathJax-Span-194" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -3.873em; left: 0.717em;"><span class="mn" id="MathJax-Span-195" style="font-size: 70.7%; font-family: STIXMathJax_Main;">1</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.203em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.23em; border-left: 0px solid; width: 0px; height: 1.059em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-33">A_1</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-34-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>10</mn><mo>,</mo><mn>100</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-196" style="width: 4.169em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.592em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.719em, 1003.54em, 2.859em, -1000em); top: -2.538em; left: 0em;"><span class="mrow" id="MathJax-Span-197"><span class="mo" id="MathJax-Span-198" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-199" style="font-family: STIXMathJax_Main;">10</span><span class="mo" id="MathJax-Span-200" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-201" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">100</span><span class="mo" id="MathJax-Span-202" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.538em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.261em; border-left: 0px solid; width: 0px; height: 1.101em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>10</mn><mo>,</mo><mn>100</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-34">(10,100)</script>, <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-35-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>2</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-203" style="width: 1.343em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.149em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.392em, 1001.15em, 2.497em, -1000em); top: -2.203em; left: 0em;"><span class="mrow" id="MathJax-Span-204"><span class="msubsup" id="MathJax-Span-205"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.212em, 1000.69em, 4.167em, -1000em); top: -4.023em; left: 0em;"><span class="mi" id="MathJax-Span-206" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -3.873em; left: 0.717em;"><span class="mn" id="MathJax-Span-207" style="font-size: 70.7%; font-family: STIXMathJax_Main;">2</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.203em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.23em; border-left: 0px solid; width: 0px; height: 1.059em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-35">A_2</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-36-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>100</mn><mo>,</mo><mn>5</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-208" style="width: 3.642em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.113em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.707em, 1003.07em, 2.859em, -1000em); top: -2.538em; left: 0em;"><span class="mrow" id="MathJax-Span-209"><span class="mo" id="MathJax-Span-210" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-211" style="font-family: STIXMathJax_Main;">100</span><span class="mo" id="MathJax-Span-212" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-213" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">5</span><span class="mo" id="MathJax-Span-214" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.538em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.261em; border-left: 0px solid; width: 0px; height: 1.115em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>100</mn><mo>,</mo><mn>5</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-36">(100,5)</script> et <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-37-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>3</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-215" style="width: 1.343em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.149em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.392em, 1001.15em, 2.507em, -1000em); top: -2.203em; left: 0em;"><span class="mrow" id="MathJax-Span-216"><span class="msubsup" id="MathJax-Span-217"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.212em, 1000.69em, 4.167em, -1000em); top: -4.023em; left: 0em;"><span class="mi" id="MathJax-Span-218" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -3.873em; left: 0.717em;"><span class="mn" id="MathJax-Span-219" style="font-size: 70.7%; font-family: STIXMathJax_Main;">3</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.203em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.241em; border-left: 0px solid; width: 0px; height: 1.07em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>3</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-37">A_3</script> de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-38-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo stretchy=&quot;false&quot;>(</mo><mn>5</mn><mo>,</mo><mn>50</mn><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-220" style="width: 3.02em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.586em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.707em, 1002.54em, 2.859em, -1000em); top: -2.538em; left: 0em;"><span class="mrow" id="MathJax-Span-221"><span class="mo" id="MathJax-Span-222" style="font-family: STIXMathJax_Main;">(</span><span class="mn" id="MathJax-Span-223" style="font-family: STIXMathJax_Main;">5</span><span class="mo" id="MathJax-Span-224" style="font-family: STIXMathJax_Main;">,</span><span class="mn" id="MathJax-Span-225" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">50</span><span class="mo" id="MathJax-Span-226" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.538em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.261em; border-left: 0px solid; width: 0px; height: 1.115em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>5</mn><mo>,</mo><mn>50</mn><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-38">(5,50)</script> et <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-39-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>4</mn></msub></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-227" style="width: 1.343em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.149em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.392em, 1001.15em, 2.497em, -1000em); top: -2.203em; left: 0em;"><span class="mrow" id="MathJax-Span-228"><span class="msubsup" id="MathJax-Span-229"><span style="display: inline-block; position: relative; width: 1.146em; height: 0px;"><span style="position: absolute; clip: rect(3.212em, 1000.69em, 4.167em, -1000em); top: -4.023em; left: 0em;"><span class="mi" id="MathJax-Span-230" style="font-family: STIXMathJax_Normal; font-style: italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -3.873em; left: 0.717em;"><span class="mn" id="MathJax-Span-231" style="font-size: 70.7%; font-family: STIXMathJax_Main;">4</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.203em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.23em; border-left: 0px solid; width: 0px; height: 1.059em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>4</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-39">A_4</script> de taille $(50, 200).</a></div><div class="lev2 toc-item"><a href="#Plus-longue-sous-séquence-commune" data-toc-modified-id="Plus-longue-sous-séquence-commune-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Plus longue sous séquence commune</a></div><div class="lev2 toc-item"><a href="#Plus-longue-sous-séquence-croissante" data-toc-modified-id="Plus-longue-sous-séquence-croissante-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Plus longue sous séquence croissante</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Bellman-Ford" data-toc-modified-id="Algorithme-de-Bellman-Ford-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Algorithme de Bellman-Ford</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Floyd-Warshall" data-toc-modified-id="Algorithme-de-Floyd-Warshall-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Algorithme de Floyd-Warshall</a></div><div class="lev2 toc-item"><a href="#Résolution-du-problème-du-sac-à-dos-par-programmation-dynamique" data-toc-modified-id="Résolution-du-problème-du-sac-à-dos-par-programmation-dynamique-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Résolution du problème du sac à dos par programmation dynamique</a></div><div class="lev2 toc-item"><a href="#Mémoïzation-générique" data-toc-modified-id="Mémoïzation-générique-27"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Mémoïzation générique</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-28"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Conclusion</a></div>

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
# 
# Je ne rentre pas dans les détails, allez voir [sur Internet](https://fr.wikipedia.org/wiki/Plus_longue_sous-s%C3%A9quence_commune), ou notamment des développements préparés par des élèves de l'ENS de Rennes candidat-e-s à l'agrégation de mathématiques option informatique : [ici](https://minerve.ens-rennes.fr/images/Dvt_plsc.pdf) ou [ici](https://minerve.ens-rennes.fr/index.php/Plus_longue_sous-s%C3%A9quence_commune).

# In[13]:


def longest_common_subsequence(x, y):
    """longest common subsequence

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
# ## Plus longue sous séquence croissante

# On traite le sous-problème suivant : $L(k)$ est la longueur de la plus longue sous séquence croissante de $[a_1,\dots,a_k]$.
# 
# $$L(1) = 1$$
# $$\forall k > 0, L(k+1) = \max(L(k), \max(L(i) + 1 : a[sol[i][-1]] <= a[k+1], i <= k))$$
# 
# C'est donc très facile d'écrire la solution :

# In[62]:


def longest_increasing_sequence(a):
    n = len(a)
    L = [0] * n
    sol = [[i] for i in range(n)]
    # L[i] = length of longer increasing sequence of a[0]..a[i]
    L[0] = 1
    sol[0] = [0]  # just <a[0]> is increasing for a[0]..a[0]
    for j in range(1, n):
        # L[j] = max(L[j-1], max(L[i]+1 for i < j such that a[sol[i][-1]] <= a[j]))
        ell = 1
        for i in range(j):
            if a[sol[i][-1]] <= a[j] and L[i] + 1 > ell:
                ell = L[i] + 1
                sol[j] = sol[i] + [j]  # sol of a[0]..a[i] + a[j]
        if ell < L[j-1]:
            ell = L[j-1]
            sol[j] = sol[i][::]
        L[j] = ell
    return [a[i] for i in sol[n-1]], sol[n-1], max(L)


# Avec l'exemple utilisé en cours :

# In[59]:


sequence = [19, 1, 9, 27, 26]


# In[61]:


for i in range(1, len(sequence) + 1):
    print("Pour la séquence", sequence[:i], "la plus longue sous séquence croissante est", longest_increasing_sequence(sequence[:i]))


# ---
# ## Algorithme de Bellman-Ford
# 
# **Chemin de $k$ sommets** : on considère le sous-problème $P(k)$ suivant : chercher la longueur des plus courts chemins comportant au plus $k$ sommets ($k \in \{1,\dots,n\}$).
# 
# On fixe l'origine des chemins, $s$ ; on note $\delta(k, t)$ la longueur minimale d'un chemin d'au plus $k$ arcs de $s$ à $t$. On a la relation de récurrence suivante :
# 
# $$\delta(0, t) = \begin{cases}
#     0 & \textrm{ si } s=t \\
#     \infty & \textrm { sinon.}
#      \end{cases}$$
# $$\delta(k + 1, t) = \min(\delta(k, t), \min \{\delta(k, u) + w(u,t), u\in S \}) $$
# 
# Cela donne l'algorithme suivant, qui fixe $s\in S$ le sommet de départ.
# L'algorithme de Bellman-Ford s'exécute en mémoire $\mathcal{O}(|S|)$ et en temps $\mathcal{O}(|S| * |A|)$.
# 
# Donc avec tous les sommets $s\in S$ différents, cela donne $\mathcal{O}(|S|^2 |A|) \leq \mathcal{O}(|S|^4)$.

# In[63]:


def bellman_ford(graph, weight, source=0):
    """ Single source shortest paths by Bellman-Ford

    :param graph: directed graph in listlist or listdict format
    :param weight: can be negative.
                   in matrix format or same listdict graph
    :returns: distance table, precedence table, bool
    :explanation: bool is True if a negative circuit is
                  reachable from the source, circuits
                  can have length 2.
    :complexity: `O(|S|*|A|)`
    """
    n = len(graph)
    dist = [float('inf')] * n
    prec = [None] * n
    dist[source] = 0
    # this loop is in O(|S|) nb of vertex
    for nb_iterations in range(n):
        changed = False
        # these two loops are in O(\sum_u degree(u)) = O(|A|) nb of edges
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
# 
# 
# **Chemin empruntant les sommets $\{1, \ldots, k\}$**
# On suppose que $S=\{1, \ldots, n\}$ (quitte à ré-étiqueter les sommets), on s'intéresse au sous-problème $P(k)$ suivant~: chercher la longueur des plus courts chemins dont les sommets intermédiaires sont dans $\{1, \ldots, k\}$.
# 
# On note maintenant $\delta(k, s, t)$ la longueur minimale d'un chemin de $s$ à
# $t$ dont les sommets intermédiaires sont dans $\{1, \ldots, k\}$.
# 
# On a la relation de récurrence $\delta(k, s, t) = \min(\delta(k-1, s, t), \delta(k-1, s, k) + \delta(k-1, k, t))$
# et le cas simple
# $$\delta(0, s, t) =
#   \begin{cases}
#     0  \textrm{ si } s=t \\
#     w(s,t) & \textrm { sinon.}
#   \end{cases}$$
# 
# Cela donne l'algorithme suivant.
# L'algorithme de Floyd-Warshall s'exécute en mémoire $\mathcal{O}(|S|^2)$ et en temps $\mathcal{O}(|S|^3)$.
# 
# > Cherchez par vous même le lien entre produit de matrice (dans le sous-anneau "tropical" $(\mathbb{R}, \min, +)$) et l'algorithme de Floyd-Warshall.

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
