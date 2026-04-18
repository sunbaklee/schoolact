from flask import Flask, request, jsonify

app = Flask(__name__)

# 가상의 메모리 데이터베이스 (서버가 꺼지면 데이터는 사라집니다)
schedules = [
    {"id": 1, "title": "백엔드 개발 회의", "date": "2026-04-20", "done": False},
    {"id": 2, "title": "REST API 복습하기", "date": "2026-04-21", "done": False}
]
next_id = 3 # 다음에 생성될 스케줄의 ID 번호

# --- 1. 스케줄 목록 전체 조회 (Read) ---
# HTTP 메서드: GET
@app.route('/api/schedules', methods=['GET'])
def get_schedules():
    # 저장된 모든 스케줄을 JSON 형태로 반환합니다.
    return jsonify({"schedules": schedules}), 200

# --- 2. 특정 스케줄 하나만 조회 (Read) ---
# HTTP 메서드: GET
@app.route('/api/schedules/<int:schedule_id>', methods=['GET'])
def get_schedule(schedule_id):
    # 요청받은 ID와 일치하는 스케줄을 찾습니다.
    schedule = next((s for s in schedules if s['id'] == schedule_id), None)
    
    if schedule:
        return jsonify(schedule), 200
    else:
        return jsonify({"error": "해당 스케줄을 찾을 수 없습니다."}), 404

# --- 3. 새로운 스케줄 생성 (Create) ---
# HTTP 메서드: POST
@app.route('/api/schedules', methods=['POST'])
def create_schedule():
    global next_id
    # 클라이언트가 보낸 JSON 데이터를 파이썬 딕셔너리로 변환하여 받습니다.
    data = request.get_json()
    
    new_schedule = {
        "id": next_id,
        "title": data.get('title', '제목 없음'),
        "date": data.get('date', ''),
        "done": False
    }
    
    schedules.append(new_schedule)
    next_id += 1
    
    # 생성된 데이터와 함께 성공 상태 코드(201 Created)를 반환합니다.
    return jsonify(new_schedule), 201

# --- 4. 기존 스케줄 수정 (Update) ---
# HTTP 메서드: PUT
@app.route('/api/schedules/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    schedule = next((s for s in schedules if s['id'] == schedule_id), None)
    
    if not schedule:
        return jsonify({"error": "해당 스케줄을 찾을 수 없습니다."}), 404

    data = request.get_json()
    
    # 전달받은 데이터가 있으면 덮어씌우고, 없으면 기존 값을 유지합니다.
    schedule['title'] = data.get('title', schedule['title'])
    schedule['date'] = data.get('date', schedule['date'])
    schedule['done'] = data.get('done', schedule['done'])
    
    return jsonify(schedule), 200

# --- 5. 특정 스케줄 삭제 (Delete) ---
# HTTP 메서드: DELETE
@app.route('/api/schedules/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    global schedules
    
    # 삭제하려는 ID를 제외한 나머지 스케줄만 모아서 새로운 리스트를 만듭니다.
    initial_length = len(schedules)
    schedules = [s for s in schedules if s['id'] != schedule_id]
    
    if len(schedules) < initial_length:
        return jsonify({"message": f"{schedule_id}번 스케줄이 삭제되었습니다."}), 200
    else:
        return jsonify({"error": "해당 스케줄을 찾을 수 없습니다."}), 404

# --- 서버 실행 ---
if __name__ == '__main__':
    print("REST API 서버가 시작됩니다! (http://127.0.0.1:5000)")
    app.run(debug=True, port=5000)
