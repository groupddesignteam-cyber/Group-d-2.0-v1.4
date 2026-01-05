
import os

file_path = r'c:\Users\WD\Downloads\그룹웨어\그룹디2.0-2\package.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find start of script block
start_marker = '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>'
end_marker = '</body>'

if start_marker in content:
    pre_script = content.split(start_marker)[0]
    # We want to replace everything from start_marker to </body>
    # But wait, we should preserve the </body> tag.
    
    new_script = """<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({ duration: 800, once: true });
        
        // --- Tabs ---
        function switchTab(tabId, btn) {
            document.querySelectorAll('.tab-content').forEach(el => {
                el.classList.add('hidden');
                el.classList.remove('block');
            });
            const target = document.getElementById(tabId);
            if(target) {
                target.classList.remove('hidden');
                target.classList.add('block');
            }
            document.querySelectorAll('.tab-btn').forEach(b => {
                b.setAttribute('data-state', 'inactive');
                b.classList.remove('active');
            });
            if(btn) {
                btn.setAttribute('data-state', 'active');
                btn.classList.add('active');
            }
        }

        // --- Modals ---
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

        function openModal() {
            const overlay = document.getElementById('modal-overlay');
            overlay.style.display = 'flex';
            setTimeout(() => overlay.classList.add('show'), 10);
            calculateTotal(); 
        }
        function closeModal(e) { if (e.target.id === 'modal-overlay') closeModalNow(); }
        function closeModalNow() {
            const overlay = document.getElementById('modal-overlay');
            overlay.classList.remove('show');
            setTimeout(() => overlay.style.display = 'none', 300);
        }

        // --- Logic ---
        function selectRadio(element, groupName, price, name) {
            const input = element.querySelector('input');
            
            // Toggle off if already selected? No, usually radio switch.
            // But verify if user clicks enabled card again.
            // For now standard radio behavior.
            document.querySelectorAll(`input[name="${groupName}"]`).forEach(inp => {
                inp.closest('.card-dark').classList.remove('selected');
                inp.checked = false;
            });
            
            element.classList.add('selected');
            input.checked = true;
            input.dataset.price = price;
            input.dataset.name = name;
            input.dataset.type = 'monthly';
            calculateTotal();
        }

        function updateCount(btn, delta) {
            const countSpan = btn.parentElement.querySelector('.count-num');
            let count = parseInt(countSpan.innerText);
            count += delta;
            if (count < 0) count = 0;

            countSpan.innerText = count;
            const card = btn.closest('.card-dark'); 

            if (card && !card.classList.contains('no-style')) {
                if (count > 0) card.classList.add('selected');
                else card.classList.remove('selected');
            }
            if (count > 0) countSpan.classList.add('active');
            else countSpan.classList.remove('active');

            calculateTotal();
        }

        function toggleBenefit(cb, name) {
            calculateTotal();
        }

        function calculateTotal() {
            let monthly = 0;
            let oneoff = 0;
            const selectedList = [];

            // 1. Monthly (Radio)
            const radio = document.querySelector('input[name="management"]:checked');
            if (radio) {
                const p = parseInt(radio.dataset.price || 0);
                monthly += p;
                selectedList.push(`[월간] ${radio.dataset.name} (${p.toLocaleString()}원)`);
            }

            // 2. Counters (A la Carte + Initial Setup Planning)
            document.querySelectorAll('.count-num').forEach(span => {
                const count = parseInt(span.innerText);
                if (count > 0) {
                    const price = parseInt(span.dataset.price);
                    const name = span.dataset.name;
                    oneoff += price * count;
                    selectedList.push(`[건별] ${name} x ${count} (${(price * count).toLocaleString()}원)`);
                }
            });

            // 3. Benefit (Checkbox)
            const benefitCb = document.getElementById('setup-benefit');
            if (benefitCb && benefitCb.checked) {
                selectedList.push(`[혜택] 디자인 초기 패키지 지원 (0원)`);
            }

            // Update UI
            document.getElementById('total-monthly').innerText = monthly.toLocaleString();
            document.getElementById('total-oneoff').innerText = oneoff.toLocaleString();
            document.getElementById('modal-monthly').innerText = monthly.toLocaleString();
            document.getElementById('modal-oneoff').innerText = oneoff.toLocaleString();

            const listEl = document.getElementById('selected-list');
            if (listEl) {
                listEl.innerHTML = selectedList.length > 0
                    ? selectedList.map(item => `<li>${item}</li>`).join('')
                    : '<li class="text-slate-500">선택된 항목이 없습니다.</li>';
            }
        }

        // --- Submit ---
        const GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbx9drSsnbn0oR_r2AWgKGnafHIOfXi-JyFqGNWaFlDBrtb3AOITgr02p6qjDLtw7DnouQ/exec";

        function submitConsultation() {
            const hospitalName = document.getElementById('hospital-name').value.trim();
            const userName = document.getElementById('user-name').value.trim();
            const userPhone = document.getElementById('user-phone').value.trim();
            const remarks = document.getElementById('user-remarks').value.trim();

            if (!hospitalName || !userName || !userPhone) {
                alert("모든 정보를 입력해주세요.");
                return;
            }

            const btn = document.getElementById('submit-btn');
            const originalText = btn.innerText;
            btn.disabled = true;
            btn.innerText = "전송 중...";

            // Gather Data
            const listItems = document.querySelectorAll('#selected-list li');
            const selectedListText = Array.from(listItems)
                                         .map(li => li.innerText)
                                         .filter(t => !t.includes('없습니다'))
                                         .join(', ');
            
            const payload = {
                hospitalName: hospitalName,
                customerName: userName,
                phone: userPhone,
                monthlyPackage: document.querySelector('input[name="management"]:checked')?.dataset.name || "미선택",
                oneoffPackage: "상세항목참조", 
                selectedItems: selectedListText || "선택없음",
                totalMonthly: document.getElementById('total-monthly').innerText,
                totalOneoff: document.getElementById('total-oneoff').innerText,
                remarks: remarks
            };

            if (!GOOGLE_SCRIPT_URL) {
                 alert("스크립트 URL 미설정");
                 btn.disabled = false; return;
            }

            fetch(GOOGLE_SCRIPT_URL, {
                method: 'POST',
                body: JSON.stringify(payload),
                mode: 'no-cors',
                headers: { 'Content-Type': 'application/json' }
            }).then(() => {
                alert("신청이 완료되었습니다.");
                closeModalNow();
                btn.disabled = false;
                btn.innerText = originalText;
                document.getElementById('hospital-name').value='';
                document.getElementById('user-name').value='';
                document.getElementById('user-phone').value='';
                document.getElementById('user-remarks').value='';
            }).catch(err => {
                console.error(err);
                alert("전송 실패. 다시 시도해주세요.");
                btn.disabled = false;
                btn.innerText = originalText;
            });
        }
        
        window.addEventListener('load', () => {
             calculateTotal();
        });

    </script>
"""
    
    final_content = pre_script + new_script + "\n</body>\n</html>"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
else:
    print("Could not find script start marker")

