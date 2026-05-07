"""
기상청 날씨 캘린더 - 위치 설정 파일
======================================
원하는 위치의 설정값을 GitHub Secrets에 복사하여 사용하세요.

설정 항목:
  KMA_NX        : 기상청 격자 X좌표
  KMA_NY        : 기상청 격자 Y좌표
  LOCATION_NAME : 캘린더에 표시될 위치명
  REG_ID_TEMP   : 중기기온예보 구역코드
  REG_ID_LAND   : 중기육상예보 구역코드

중기예보 구역코드 전체 목록:
  https://apihub.kma.go.kr → 기술문서 → 중기예보 구역코드 참고
"""

LOCATIONS = {

    # ─────────────── 광주광역시 ───────────────
    "광주광역시": {
        "KMA_NX": 58,
        "KMA_NY": 74,
        "LOCATION_NAME": "광주광역시",
        "REG_ID_TEMP": "11F20501",   # 중기기온: 광주
        "REG_ID_LAND": "11F20000",   # 중기육상: 전라남도(내륙)
        "비고": "광주 서구·남구·북구·광산구 공통 사용 가능",
    },

    # ─────────────── 전남 동부권 ───────────────
    "완도군": {
        "KMA_NX": 57,
        "KMA_NY": 68,
        "LOCATION_NAME": "완도군",
        "REG_ID_TEMP": "11H20901",   # 중기기온: 완도
        "REG_ID_LAND": "11H20000",   # 중기육상: 전라남도(해안)
        "비고": "완도·진도·해남 해안권",
    },
    "화순군": {
        "KMA_NX": 61,
        "KMA_NY": 74,
        "LOCATION_NAME": "화순군",
        "REG_ID_TEMP": "11H20802",   # 중기기온: 순천(인근)
        "REG_ID_LAND": "11H20000",   # 중기육상: 전라남도(해안)
        "비고": "화순·나주 권역",
    },
    "담양군": {
        "KMA_NX": 61,
        "KMA_NY": 78,
        "LOCATION_NAME": "담양군",
        "REG_ID_TEMP": "11F20601",   # 중기기온: 장성(인접)
        "REG_ID_LAND": "11F20000",   # 중기육상: 전라남도(내륙)
        "비고": "담양·곡성 권역",
    },

    # ─────────────── 전남 서부권 ───────────────
    "장성군": {
        "KMA_NX": 56,
        "KMA_NY": 77,
        "LOCATION_NAME": "장성군",
        "REG_ID_TEMP": "11F20601",   # 중기기온: 장성
        "REG_ID_LAND": "11F20000",   # 중기육상: 전라남도(내륙)
        "비고": "장성·함평 권역",
    },
    "영광군": {
        "KMA_NX": 52,
        "KMA_NY": 77,
        "LOCATION_NAME": "영광군",
        "REG_ID_TEMP": "11F20401",   # 중기기온: 고창(인접, 전북)
        "REG_ID_LAND": "11F20000",   # 중기육상: 전라남도(내륙)
        "비고": "영광·함평 해안 서부권",
    },
    "목포시": {
        "KMA_NX": 50,
        "KMA_NY": 67,
        "LOCATION_NAME": "목포시",
        "REG_ID_TEMP": "11H20101",   # 중기기온: 목포
        "REG_ID_LAND": "11H20000",   # 중기육상: 전라남도(해안)
        "비고": "목포·무안 권역",
    },
    "여수시": {
        "KMA_NX": 73,
        "KMA_NY": 66,
        "LOCATION_NAME": "여수시",
        "REG_ID_TEMP": "11H20301",   # 중기기온: 여수
        "REG_ID_LAND": "11H20000",   # 중기육상: 전라남도(해안)
        "비고": "여수·순천·광양 권역",
    },
    "순천시": {
        "KMA_NX": 70,
        "KMA_NY": 70,
        "LOCATION_NAME": "순천시",
        "REG_ID_TEMP": "11H20802",   # 중기기온: 순천
        "REG_ID_LAND": "11H20000",   # 중기육상: 전라남도(해안)
        "비고": "순천·광양 권역",
    },

    # ─────────────── 주요 광역시 (참고용) ───────────────
    "서울": {
        "KMA_NX": 60,
        "KMA_NY": 127,
        "LOCATION_NAME": "서울",
        "REG_ID_TEMP": "11B10101",
        "REG_ID_LAND": "11B00000",
        "비고": "서울 전역",
    },
    "부산": {
        "KMA_NX": 98,
        "KMA_NY": 76,
        "LOCATION_NAME": "부산",
        "REG_ID_TEMP": "11H20201",
        "REG_ID_LAND": "11H20000",
        "비고": "부산 전역",
    },
}


def print_location_info(name: str):
    """지정 위치의 GitHub Secrets 설정값 출력"""
    loc = LOCATIONS.get(name)
    if not loc:
        print(f"❌ '{name}' 위치를 찾을 수 없습니다.")
        print(f"   사용 가능한 위치: {list(LOCATIONS.keys())}")
        return
    print(f"\n📍 [{name}] GitHub Secrets 설정값")
    print("=" * 45)
    print(f"  KMA_NX        : {loc['KMA_NX']}")
    print(f"  KMA_NY        : {loc['KMA_NY']}")
    print(f"  LOCATION_NAME : {loc['LOCATION_NAME']}")
    print(f"  REG_ID_TEMP   : {loc['REG_ID_TEMP']}")
    print(f"  REG_ID_LAND   : {loc['REG_ID_LAND']}")
    print(f"  비고           : {loc.get('비고', '-')}")
    print("=" * 45)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print_location_info(sys.argv[1])
    else:
        print("사용법: python locations.py <위치명>")
        print(f"사용 가능한 위치: {list(LOCATIONS.keys())}")
