


# Đưa ra 2 test case để chứng minh API đang sai logic
# Test case 1: Hãy chuyển vào mã sinh viên SV001 và khóa học 1 thì nó sẽ báo trùng học viên đã đăng ký khóa học này
# Test case 2: Hãy chuyền vào mã sinh viên SV002 và khóa học 1 thì nó sẽ báo trùng học viên đã đăng ký khóa học này
# Phần 2 : Sửa lại source code



from fastapi import FastAPI , HTTPException , status
from pydantic import BaseModel
app = FastAPI()
enrollments = [
    {
        "id": 1,
        "student_id": "SV001",
        "course_id": 1
    },
    {
        "id": 2,
        "student_id": "SV002",
        "course_id": 1
    }
]
class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: int
@app.post("/enrollments" , status_code = status.HTTP_201_CREATED)
def create_enrollment(enrollment: EnrollmentCreate):
    # Kiểm tra đã đăng ký khóa học chưa
    if any(
        item["student_id"] == enrollment.student_id
        and item["course_id"] == enrollment.course_id
        for item in enrollments
    ):
        raise HTTPException(
            status_code=409,
            detail="Học viên đã đăng ký khóa học này"
        )
    new_enrollment = {
        "id": len(enrollments) + 1,
        "student_id": enrollment.student_id,
        "course_id": enrollment.course_id
    }
    enrollments.append(new_enrollment)
    return {
        "message": "Enroll successfully",
        "data": new_enrollment
    }



