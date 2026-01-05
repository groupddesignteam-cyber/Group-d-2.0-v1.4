
import re

file_path = r"c:\Users\WD\Downloads\그룹웨어\그룹디2.0-2\package.html"

# The new content for the Options Tab
# Copied from previous step but verified.
new_tab_content = """        <!-- 2. Options (A la Carte) -->
        <div id="tab-options" class="tab-content hidden animate-fade-in">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                
                <!-- A. Ads Management -->
                <div>
                    <h3 class="text-lg font-bold text-white mb-4 border-l-4 border-amber-500 pl-3">A. 광고 운영 대행료 <span class="text-xs font-normal text-slate-500 ml-2">(광고비 별도 충전)</span></h3>
                    <div class="space-y-3">
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">네이버 플레이스 광고</span>
                            <div class="flex items-center gap-4">
                                <span class="text-amber-400 font-bold text-sm">10만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="100000" data-name="대행: 플레이스 광고" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">네이버 파워링크 (텍스트형)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-amber-400 font-bold text-sm">10만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="100000" data-name="대행: 파워링크(텍스트)" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">네이버 파워링크 (이미지형)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-amber-400 font-bold text-sm">20만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="200000" data-name="대행: 파워링크(이미지)" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">네이버 GFA (성과형)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-amber-400 font-bold text-sm">15만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="150000" data-name="대행: GFA 성과형" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">SNS/구글/유튜브 광고</span>
                            <div class="flex items-center gap-4">
                                <span class="text-amber-400 font-bold text-sm">30만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="300000" data-name="대행: SNS/구글/유튜브" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- B. Blog & Viral -->
                <div>
                     <h3 class="text-lg font-bold text-white mb-4 border-l-4 border-emerald-500 pl-3">B. 블로그 & 바이럴</h3>
                     <div class="space-y-3">
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm card-label">간단 포스팅 (1회성)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm price-tag">2만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="20000" data-name="블로그: 간단 포스팅" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm card-label">커스텀 포스팅 (Standard)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm price-tag">7.5만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="75000" data-name="블로그: 커스텀 포스팅" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm card-label">브랜딩/다이나믹 포스팅</span>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm price-tag">30만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="300000" data-name="블로그: 다이나믹 포스팅" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm card-label">서로이웃 관리 (월)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm price-tag">5만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="50000" data-name="블로그: 이웃관리(월)" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm card-label">블로그 관리 대행 (간단, 월)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm price-tag">15만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="150000" data-name="블로그: 관리대행(간단)" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <div>
                                <span class="text-white font-bold text-sm block">지식인 (질문+답변)</span>
                                <span class="text-xs text-slate-500">일반 5천 / 자문자답 1만</span>
                            </div>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm price-tag">1만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="10000" data-name="바이럴: 지식인" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                         <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm card-label">맘카페 (정보성/Hot딜)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm price-tag">20만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="200000" data-name="바이럴: 맘카페" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                     </div>
                </div>

                <!-- C. Web & Design -->
                <div>
                    <h3 class="text-lg font-bold text-white mb-4 border-l-4 border-blue-500 pl-3">C. 상세페이지 & 웹 구축</h3>
                    <div class="space-y-3">
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <div>
                                <span class="text-white font-bold text-sm block">상세페이지 Standard (간단)</span>
                                <span class="text-xs text-slate-500">박스/파우치 등 단품/이벤트용</span>
                            </div>
                            <div class="flex items-center gap-4">
                                <span class="text-blue-400 font-bold text-sm">50만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="500000" data-name="상세: Standard" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <div>
                                <span class="text-white font-bold text-sm block">상세페이지 Deluxe (일반)</span>
                                <span class="text-xs text-slate-500">10개 섹션, GIF 1개 포함</span>
                            </div>
                            <div class="flex items-center gap-4">
                                <span class="text-blue-400 font-bold text-sm">150만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="1500000" data-name="상세: Deluxe" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group border-blue-500/30">
                            <div>
                                <span class="text-white font-bold text-sm block">상세페이지 Premium (고급)</span>
                                <span class="text-xs text-slate-500">기획 포함, 고퀄리티</span>
                            </div>
                            <div class="flex items-center gap-4">
                                <span class="text-blue-400 font-bold text-sm">200만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="2000000" data-name="상세: Premium" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">이벤트 랜딩 (1 Page)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-blue-400 font-bold text-sm">50만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="500000" data-name="웹: 이벤트 랜딩" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">핵심 랜딩/홈페이지 (4 Page)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-blue-400 font-bold text-sm">150만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="1500000" data-name="웹: 홈페이지(4P)" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">블로그 스킨 디자인 (PC+MB)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-blue-400 font-bold text-sm">15만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="150000" data-name="디자인: 블로그 스킨" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                         <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <div>
                                <span class="text-white font-bold text-sm block">로고(CI/BI) 개발</span>
                                <span class="text-xs text-slate-500">간단 텍스트형: 5만원</span>
                            </div>
                            <div class="flex items-center gap-4">
                                <span class="text-blue-400 font-bold text-sm">50만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="500000" data-name="디자인: 로고" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                         <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">로고 (간단 텍스트형)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-blue-400 font-bold text-sm">5만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="50000" data-name="디자인: 로고(텍스트)" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- D. Video -->
                <div>
                    <h3 class="text-lg font-bold text-white mb-4 border-l-4 border-pink-500 pl-3">D. 영상 제작</h3>
                    <div class="space-y-3">
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">숏폼 (일반) <span class="text-xs font-normal text-slate-500">6건↑촬영무료</span></span>
                            <div class="flex items-center gap-4">
                                <span class="text-pink-400 font-bold text-sm">30만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="300000" data-name="영상: 숏폼(일반)" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                         <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">숏폼 (셀프/정보성)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-pink-400 font-bold text-sm">25만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="250000" data-name="영상: 숏폼(셀프)" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">유튜브 롱폼 (인터뷰/QnA)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-pink-400 font-bold text-sm">150만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="1500000" data-name="영상: 롱폼" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">브랜딩 필름</span>
                            <div class="flex items-center gap-4">
                                <span class="text-pink-400 font-bold text-sm">300만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="3000000" data-name="영상: 브랜딩필름" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                         <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">촬영 출장비 (2인 기준)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-white font-bold text-sm">50만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="500000" data-name="영상: 출장비" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Using known strings from previous view_file (Step 1442)
# Start is line 390
# End is line 715
# We have to be very careful to target unique strings.

start_str = '<!-- 2. Options (A la Carte) -->'
end_str = '<!-- 3. Initial Setup -->'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    print(f"Found block: Start {start_idx}, End {end_idx}")
    
    # Preserve formatting, insert new content plus a few newlines
    updated_content = content[:start_idx] + new_tab_content + "\n\n        " + content[end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("SUCCESS: File updated.")
else:
    print(f"ERROR: Could not find markers. Start: {start_idx}, End: {end_idx}")
