
import os

file_path = r'c:\Users\WD\Downloads\그룹웨어\그룹디2.0-2\package.html'

# 1. Read Original File
with open(file_path, 'r', encoding='utf-8') as f:
    original_content = f.read()

# 2. Extract Parts
# We need everything BEFORE <main> and everything AFTER </main>
try:
    head_part = original_content.split('<main class="max-w-7xl mx-auto px-4">')[0]
    rest = original_content.split('</main>')[1]
except IndexError:
    # Fallback if class changed
    head_part = original_content.split('<main')[0]
    rest = original_content.split('</main>')[1]
    # Re-add tag if lost (but standard split keeps delimiters? No, split removes them)
    # Actually split removes the delimiter.
    # So head_part is up to <main...
    # We should reconstruct the tag structure.
    pass

# Clean up head_part to ensure it ends cleanly
head_part = head_part.strip()

# 3. Define New Main Content
new_main_html = """
    <main class="max-w-7xl mx-auto px-4 min-h-[600px]">

        <!-- Tabs Navigation -->
        <div class="flex flex-wrap justify-center gap-2 md:gap-4 mb-10" data-aos="fade-up">
            <button onclick="switchTab('tab-monthly', this)" 
                class="tab-btn active px-6 py-3 rounded-full bg-slate-800 text-slate-400 font-bold border border-slate-700 hover:bg-slate-700 transition-all text-sm md:text-base data-[state=active]:bg-blue-600 data-[state=active]:text-white data-[state=active]:border-blue-500 shadow-lg">
                월간 관리 솔루션
            </button>
            <button onclick="switchTab('tab-options', this)" 
                class="tab-btn px-6 py-3 rounded-full bg-slate-800 text-slate-400 font-bold border border-slate-700 hover:bg-slate-700 transition-all text-sm md:text-base data-[state=active]:bg-blue-600 data-[state=active]:text-white data-[state=active]:border-blue-500 shadow-lg">
                옵션 및 단품 (A la Carte)
            </button>
            <button onclick="switchTab('tab-setup', this)" 
                class="tab-btn px-6 py-3 rounded-full bg-slate-800 text-slate-400 font-bold border border-slate-700 hover:bg-slate-700 transition-all text-sm md:text-base data-[state=active]:bg-blue-600 data-[state=active]:text-white data-[state=active]:border-blue-500 shadow-lg">
                초기 세팅 (Setup)
            </button>
        </div>

        <!-- 1. Monthly Plan -->
        <div id="tab-monthly" class="tab-content block animate-fade-in">
            <div class="mb-6 text-center text-slate-400 text-xs md:text-sm">
                * 모든 플랜은 <span class="text-blue-400 font-bold">세무/노무 기본 자문</span>이 포함됩니다.<br>
                * 디자인 혜택에서 홈페이지, 상세페이지, 케이스북(책자)은 제외됩니다.
                <button onclick="openDesignModal()" class="text-slate-500 underline ml-2 hover:text-white cursor-pointer">가능 품목 보기</button>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                
                <!-- Economy -->
                <div class="card-dark rounded-[2rem] p-6 flex flex-col h-full hover-green"
                     onclick="selectRadio(this, 'management', 500000, '이코노미')">
                    <input type="radio" name="management" class="item-input">
                    <div class="mb-4">
                        <span class="text-[10px] font-bold text-slate-500 bg-slate-800 px-2 py-1 rounded">Start-up</span>
                        <h3 class="text-2xl font-bold text-white mt-2">이코노미</h3>
                    </div>
                    <ul class="text-xs text-slate-300 space-y-2 mb-4 flex-1">
                        <li>• 블로그/플레이스 기본 관리</li>
                        <li>• 영수증 리뷰 (월 2회)</li>
                        <li>• 카카오 채널 기초 운영</li>
                        <li class="pt-2 border-t border-white/10 text-emerald-400">🎁 디자인 월 2건 (1장/건)</li>
                    </ul>
                    <div class="mt-auto text-right border-t border-white/10 pt-4">
                        <span class="text-2xl font-bold text-white">50</span><span class="text-sm">만원/월</span>
                    </div>
                </div>

                <!-- Basic -->
                <div class="card-dark rounded-[2rem] p-6 flex flex-col h-full hover-blue"
                     onclick="selectRadio(this, 'management', 1000000, '베이직')">
                    <input type="radio" name="management" class="item-input">
                    <div class="mb-4">
                        <span class="text-[10px] font-bold text-blue-400 bg-blue-900/30 px-2 py-1 rounded">Basic</span>
                        <h3 class="text-2xl font-bold text-white mt-2">베이직</h3>
                    </div>
                    <ul class="text-xs text-slate-300 space-y-2 mb-4 flex-1">
                        <li class="text-slate-500">✔ 이코노미 전체 포함</li>
                        <li>• <b>블로그 집중 관리</b></li>
                        <li>• 파워링크/플레이스 광고 세팅</li>
                        <li>• 주간 순위 모니터링</li>
                        <li class="pt-2 border-t border-white/10 text-blue-400">🎁 디자인 월 3건 (2장/건)</li>
                    </ul>
                    <div class="mt-auto text-right border-t border-white/10 pt-4">
                        <span class="text-2xl font-bold text-white">100</span><span class="text-sm">만원/월</span>
                    </div>
                </div>

                <!-- Standard -->
                <div class="card-dark rounded-[2rem] p-6 flex flex-col h-full border-blue-500"
                     onclick="selectRadio(this, 'management', 1500000, '스탠다드')">
                    <input type="radio" name="management" class="item-input">
                    <div class="flex justify-between mb-2">
                        <span class="text-[10px] font-bold text-blue-300 uppercase">Standard</span>
                        <span class="bg-blue-600 text-[9px] text-white px-1.5 py-0.5 rounded">BEST</span>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-4">스탠다드</h3>
                    <ul class="text-xs text-slate-300 space-y-2 mb-4 flex-1">
                        <li class="text-slate-500">✔ 베이직 전체 포함</li>
                        <li>• <b>인스타그램 채널 확장</b></li>
                        <li>• <b>전담 마케터 배정</b></li>
                        <li class="pt-2 border-t border-white/10 text-blue-300">🎁 디자인 월 4건 (2장/건)</li>
                    </ul>
                    <div class="mt-auto text-right border-t border-white/10 pt-4">
                        <span class="text-2xl font-bold text-white">150</span><span class="text-sm">만원/월</span>
                    </div>
                </div>

                <!-- Premium -->
                <div class="card-dark rounded-[2rem] p-6 flex flex-col h-full border-purple-500"
                     onclick="selectRadio(this, 'management', 2000000, '프리미엄')">
                    <input type="radio" name="management" class="item-input">
                    <div class="flex justify-between mb-2">
                        <span class="text-[10px] font-bold text-purple-400 uppercase">Premium</span>
                        <span class="bg-purple-600 text-[9px] text-white px-1.5 py-0.5 rounded">VIP</span>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-4">프리미엄</h3>
                    <ul class="text-xs text-slate-300 space-y-2 mb-4 flex-1">
                        <li class="text-slate-500">✔ 스탠다드 전체 포함</li>
                        <li>• <b>전 채널 통합 관리 (유튜브 포함)</b></li>
                        <li>• 오프라인 마케팅 연계</li>
                        <li class="pt-2 border-t border-white/10 text-purple-300">🎁 디자인 월 4건 (3장/고퀄리티)</li>
                    </ul>
                    <div class="mt-auto text-right border-t border-white/10 pt-4">
                        <span class="text-3xl font-extrabold text-white">200</span><span class="text-sm text-slate-400">만원/월</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- 2. Options (A la Carte) -->
        <div id="tab-options" class="tab-content hidden animate-fade-in">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                
                <!-- A. Management Fee -->
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

                <!-- B. Detail Page -->
                <div>
                    <h3 class="text-lg font-bold text-white mb-4 border-l-4 border-blue-500 pl-3">B. 상세페이지 제작</h3>
                    <div class="space-y-3">
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <div>
                                <span class="text-white font-bold text-sm block">Standard (간단형)</span>
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
                                <span class="text-white font-bold text-sm block">Deluxe (일반형)</span>
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
                                <span class="text-white font-bold text-sm block">Premium (고급형)</span>
                                <span class="text-xs text-slate-500">기획 포함, GIF 다수, 고퀄리티</span>
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
                    </div>
                </div>

                <!-- C. Video -->
                <div>
                    <h3 class="text-lg font-bold text-white mb-4 border-l-4 border-pink-500 pl-3">C. 영상 제작</h3>
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

                <!-- D. Blog & Other -->
                <div>
                     <h3 class="text-lg font-bold text-white mb-4 border-l-4 border-emerald-500 pl-3">D. 블로그 및 기타</h3>
                     <div class="space-y-3">
                         <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">간단 포스팅 (건당)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm">2만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="20000" data-name="블로그: 간단 포스팅" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">서로이웃 관리 (월)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm">5만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="50000" data-name="블로그: 이웃관리" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-dark rounded-xl p-4 flex justify-between items-center group">
                            <span class="text-white font-bold text-sm">이벤트 랜딩 (1 Page)</span>
                            <div class="flex items-center gap-4">
                                <span class="text-emerald-400 font-bold text-sm">50만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="500000" data-name="웹: 랜딩(1P)" data-type="oneoff">0</div>
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
                                <span class="text-emerald-400 font-bold text-sm">50만원</span>
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
                                <span class="text-emerald-400 font-bold text-sm">5만원</span>
                                <div class="counter-box">
                                    <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                                    <div class="count-num" data-price="50000" data-name="디자인: 로고(텍스트)" data-type="oneoff">0</div>
                                    <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                                </div>
                            </div>
                        </div>
                     </div>
                </div>

            </div>
        </div>

        <!-- 3. Initial Setup -->
        <div id="tab-setup" class="tab-content hidden animate-fade-in">
            <div class="max-w-3xl mx-auto space-y-6">
                 <div class="card-dark rounded-[2rem] p-8 flex flex-col md:flex-row justify-between items-center gap-6">
                     <div class="flex-1">
                         <h3 class="text-2xl font-bold text-white mb-2">온라인 플랫폼 기획비</h3>
                         <p class="text-slate-400 text-sm">블로그, 플레이스, SNS 채널 기획 및 초기 세팅 비용입니다.</p>
                     </div>
                     <div class="flex items-center gap-6">
                        <span class="text-2xl font-bold text-white">100<span class="text-sm font-normal text-slate-400">만원</span></span>
                        <div class="counter-box">
                            <div class="btn-count btn-minus" onclick="updateCount(this, -1)">-</div>
                            <div class="count-num" data-price="1000000" data-name="세팅: 플랫폼 기획" data-type="oneoff">0</div>
                            <div class="btn-count btn-plus" onclick="updateCount(this, 1)">+</div>
                        </div>
                     </div>
                 </div>

                 <div class="card-dark rounded-[2rem] p-8 bg-emerald-900/10 border-emerald-500/30">
                     <div class="flex items-center gap-3 mb-4">
                        <span class="bg-emerald-500 text-white text-xs font-bold px-2 py-1 rounded">혜택</span>
                        <h3 class="text-xl font-bold text-emerald-400">디자인 초기 패키지 무상 지원</h3>
                     </div>
                     <p class="text-slate-300 text-sm mb-4">
                         신규/기개원 계약 시 <b>필수 디자인물(명함, X배너, 원내 서식 등)</b>을 무상으로 지원해 드립니다.<br>
                         <span class="text-xs text-slate-500">* 계약 형태 및 규모에 따라 지원 품목이 상이할 수 있습니다.</span>
                     </p>
                     <div class="flex items-center gap-2">
                         <input type="checkbox" id="setup-benefit" class="w-5 h-5 accent-emerald-500" onchange="toggleBenefit(this, '디자인 초기 패키지 지원')">
                         <label for="setup-benefit" class="text-white text-sm cursor-pointer select-none">혜택 적용 요청하기 (0원)</label>
                     </div>
                 </div>
            </div>
        </div>

    </main>

    <!-- Design List Modal (Hidden by default) -->
    <div id="design-modal-overlay" class="modal-overlay" onclick="closeDesignModal(event)">
        <div class="modal-content p-8 max-w-2xl bg-[#0f101a]" onclick="event.stopPropagation()">
            <div class="flex justify-between items-center mb-6">
                <h3 class="text-xl font-bold text-white">🎨 월간 디자인 선택 가능 품목</h3>
                <button onclick="closeDesignModalNow()" class="text-slate-500 hover:text-white text-2xl">&times;</button>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-6">
                <div>
                     <h4 class="text-emerald-400 font-bold mb-3 border-b border-white/10 pb-2">온라인 디자인</h4>
                     <ul class="space-y-2 text-sm text-slate-300 list-disc pl-4">
                         <li>팝업/배너 이미지</li>
                         <li>카드뉴스</li>
                         <li>블로그 스킨 (부분)</li>
                         <li>SNS 프로필 이미지</li>
                         <li>이벤트 이미지</li>
                     </ul>
                </div>
                <div>
                     <h4 class="text-blue-400 font-bold mb-3 border-b border-white/10 pb-2">원내/인쇄물 (시안)</h4>
                     <ul class="space-y-2 text-sm text-slate-300 list-disc pl-4">
                         <li>명함 시안</li>
                         <li>대/소봉투 시안</li>
                         <li>서식류 (접수증/주의사항)</li>
                         <li>X배너/현수막 시안</li>
                         <li>DID 모니터 이미지</li>
                         <li>약력 액자 시안</li>
                     </ul>
                </div>
            </div>
            <div class="bg-rose-900/20 p-4 rounded-xl border border-rose-500/20 text-sm">
                <p class="font-bold text-rose-400 mb-1">⛔ 제외 항목 (별도 구매)</p>
                <p class="text-slate-400">홈페이지 제작, 상세페이지 제작, 케이스북(책자) 제작은 월간 디자인 혜택에 포함되지 않습니다.</p>
            </div>
        </div>
    </div>
"""

# 4. Construct Full HTML
# Also append tab script and style if needed
add_script = """
    <script>
        function switchTab(tabId, btn) {
            // Hide all tabs
            document.querySelectorAll('.tab-content').forEach(el => {
                el.classList.add('hidden');
                el.classList.remove('block');
            });
            // Show target
            const target = document.getElementById(tabId);
            if(target) {
                target.classList.remove('hidden');
                target.classList.add('block');
            }
            
            // Update buttons
            document.querySelectorAll('.tab-btn').forEach(b => {
                b.setAttribute('data-state', 'inactive');
                b.classList.remove('active'); // fallback
            });
            btn.setAttribute('data-state', 'active');
            btn.classList.add('active'); // fallback
            
            // Re-calc AOS if needed (optional)
        }

        function openDesignModal() {
            const overlay = document.getElementById('design-modal-overlay');
            overlay.style.display = 'flex';
            setTimeout(() => overlay.classList.add('show'), 10);
        }
        function closeDesignModal(e) { if (e.target.id === 'design-modal-overlay') closeDesignModalNow(); }
        function closeDesignModalNow() {
            const overlay = document.getElementById('design-modal-overlay');
            overlay.classList.remove('show');
            setTimeout(() => overlay.style.display = 'none', 300);
        }
        
        // Benefit Checkbox Logic
        function toggleBenefit(cb, name) {
            calculateTotal(); 
            // We can treat this as an item with 0 price but listed in the summary?
            // update calculateTotal to check '.card-dark input:checked'? 
            // Or just manually add logic in calculateTotal
        }
    </script>
"""

# Insert Main
final_content = head_part + new_main_html + rest

# Insert Script before closing body
if "</body>" in final_content:
    final_content = final_content.replace("</body>", add_script + "\n</body>")

# Write
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_content)
