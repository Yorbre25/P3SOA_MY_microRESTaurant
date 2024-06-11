import { HttpInterceptorFn } from '@angular/common/http';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const authToken = sessionStorage.getItem('idToken');
  if (authToken && req.method !== 'OPTIONS') {
    const authReq = req.clone({
      setHeaders: {
        Authorization: `Authorization ${authToken}`
      }
    });
    return next(authReq);
  } else {
    return next(req);
  }
  return next(req);
};
