FROM python AS stage1

RUN apt-get update &&\
    pip3 install --upgrade pip &&\
    apt-get install -y git &&\
    git clone https://github.com/AlanShmyga/BDDAPIPythonTestingExample.git /home/testingExample

WORKDIR /home/testingExample

RUN pip3 install -r requirements.txt &&\
    pip3 install allure-behave

ENV K_BASE_URL ""
ENV K_API_KEY_22 ""
ENV K_PR_KEY_22 ""

RUN behave -f allure_behave.formatter:AllureFormatter -o /home/testingExample/allure-reports ./features

FROM scratch AS export-stage
COPY --from=stage1 /home/testingExample/allure-reports .