# 📝 ระบบบันทึกใบตรวจสินค้า (QC Inspection CRUD)

เว็บแอป CRUD สำหรับบันทึกผลตรวจสินค้า:

- ค้นหา / เพิ่ม / แก้ไข / ลบ ข้อมูล
- ฟิลด์: เลขที่ใบตรวจ, รหัสสินค้า, ชื่อสินค้า, ราคา, กลิ่น, ค่า pH (0–14), สถานะ (Pass/Not Pass)

---

## 📌 ฟีเจอร์หลัก

- เพิ่มใบตรวจสินค้าใหม่ได้ผ่านฟอร์ม 2 คอลัมน์
- ค้นหาข้อมูลตาม **เลขที่, รหัสสินค้า, กลิ่น, สถานะ**
- แก้ไข / ลบ ข้อมูลได้
- มีหน้า Admin สำหรับจัดการข้อมูลหลังบ้าน
- ใช้ฐานข้อมูล PostgreSQL เก็บข้อมูลทั้งหมด

---

## 🖥️ Requirements

- [Python 3.12+](https://www.python.org/downloads/)
- [PostgreSQL 16+](https://www.postgresql.org/download/)
- Git (optional ถ้า clone repo)
- Docker/Docker Compose (option สำหรับ run DB เร็ว ๆ)

ตรวจสอบว่า Python ติดตั้งแล้ว:

```bash
python --version
```
