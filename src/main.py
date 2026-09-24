from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/bmi")
def calculate_bmi(weight: float, height: float):
    if height <= 0 or weight <= 0:
        raise HTTPException(
            status_code=400,
            detail="Рост и вес должны быть больше нуля",
        )

    bmi = weight / (height ** 2)
    return {
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 2),
    }
