export interface IRedirectResponse {
    redirect: string;
}

export interface IDataResponse {
    [key: string]: unknown;
}

export interface IResponseProcess {
    response: IRedirectResponse | IDataResponse;
}